## Configuration settings:
import os

basedir = os.path.abspath(os.path.dirname(__file__))

## ========================
## Server List:
## ------------------------
## To add a new server, insert a new line with the following format:
## server_list.append(Authentication.Server("<Server Name", "Server URL"))
## ========================
class ServerConfig(object):
    server_list = []
    ##server_list.append(["Server Name", "Server Link (including https://, and no forward slash at the end)"])

## ========================
## Authentication Information:
## ------------------------
## FOR CONVENIENCE PURPOSES DURING TESTING ONLY.
## If you choose to field up these fields, NEVER EVER SHARE YOUR CONFIG FILE!
## ========================
class AuthConfig(object):
    s1_username = "email"
    s1_password = "passowrd"
    pov_username = "peepee"
    pov_password = "poopoo"
    

## ========================
## Application-specific Settings:
## ------------------------
## ========================