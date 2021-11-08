# !WARNING!
This tools have been written during solving test task from <company_name> :)

They are not suitable to exploit real vulnerabilities.
# File_Getter_v1.0
File_Getter is tool that exploit SQL injection in file upload function to get access to Arbitrary File Reading.

### Usage
```
python file_getter.py
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

```
#### Examples:
Interactive mode with file printing, jwt printing, adding path traversal and downloading files:
```
python3 file_getter.py -interactive -jwt -printFile -addPath -download
```
FUZZ mode with file printing, jwt printing, adding path traversal and downloading files:
```
python3 file_getter.py -fuzz "validate.txt" jwt -printFile -addPath -download
```
# JWT_changer_v1.0
JWTchanger is tool to test SQL injections in JWT parameters.

It works only with ID parameter, but could be easilly upgraded to work with any parameter.
### Usage
```
python jwt_changer.py
```
---

## Requirements
```
pip install pyjwt requests
```

## Possible issues
jwt and pyJWT libraries are in conflict so you should do next:
```
pip uninstall jwt
pip uninstall pyjwt
pip install pyjwt
```
