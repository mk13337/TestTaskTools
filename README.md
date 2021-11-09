# !WARNING!
This tools have been written during solving test task from <company_name> :)

They are not suitable to exploit real vulnerabilities.
# File_Getter.py
File_Getter is tool that exploit SQL injection in file upload function to get access to Arbitrary File Reading.

## Installation
Install requirements
```
pip3 install -r requirements.txt
```
Clone repository
```
git clone https://github.com/MiichaelKlimenko/TestTaskTools/
```
Change configuration in file (you need to change only URL):
```python
##############################################
###################CONFIG#####################
URL = "http://127.0.0.1"                     # Main url to vulnerable system
filename_to_upload = "badfile.php"
file_content = "<?php phpinfo(); ?>"
user_id = 31337
is_public = 0

timeout = 2                                  # Defines time to wait when www-data has not privileges to get file

login = "admin"
mail = "admin"
role = "admin"
ip = "127.0.0.1"
##############################################
```

### Usage
```
python file_getter.py
      MODES:
                --interactive          Interactive mode to search for files manually
                --fuzz "list.txt"      Fuzz mode to search for files from list                  
          INTERACTIVE MODE
                VERBOSITY OPTIONS:      
                      --jwt            Prints JWT
                      --printFile      Prints file
                OTHER:
                      --download       Downloads file if it exists
          FUZZ MODE
                --addPath              Add path traversal "../../../../"
          --help                       Print this page

```
#### Examples:
Interactive mode with file printing, jwt printing, adding path traversal and downloading files:
```
python3 file_getter.py --interactive --jwt --printFile --addPath --download
```
FUZZ mode with file printing, jwt printing, adding path traversal and downloading files:
```
python3 file_getter.py --fuzz "validate.txt" --jwt --printFile --addPath --download
```
# JWT_changer.py
JWTchanger is tool to test SQL injections in JWT parameters.

It works only with ID parameter, but could be easilly upgraded to work with any parameter.
### Usage
```
python jwt_changer.py
```
---

## Possible issues
jwt and pyJWT libraries are in conflict so you should do next:
```
pip uninstall jwt
pip uninstall pyjwt
pip install pyjwt
```
