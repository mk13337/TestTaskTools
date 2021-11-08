# !WARNING!
This tools has been written during solving test task from <company_name> :)

They are not suitable to exploit real vulnerabilities.
# JWT_changer_v1.0
JWTchanger is tool to test SQL injections in JWT parameters.

It works only with ID parameter, but could be easilly upgraded to work with any parameter.
### Usage
```
python jwt_changer.py
```
---
# File_Getter_v1.0
File_Getter is tool that exploit SQL injection in upload.php to get access to Arbitrary File Reading.

Works only in interactive mode.
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
                FILTER OPTIONS:
                      -fs             Filter file by file size
```
## Requirements
```
pip install pyjwt requests
```
