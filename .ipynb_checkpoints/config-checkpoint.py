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
    server_list.append(["S1 Server", "https://s1.managedpdr.csintelligence.asia"])
    server_list.append(["POV Server", "https://dash.pov.managedpdr.csintelligence.asia"])
    server_list.append(["SRKK Server", "https://spdash.srkk.com"])
    server_list.append(["Eurokars Server", "https://dash.eurokars.rqt.io"])
    server_list.append(["MSI Server", "https://dash.mc.ap.rqt.io"])

## ========================
## Authentication Information:
## ------------------------
## FOR CONVENIENCE PURPOSES DURING TESTING ONLY.
## If you choose to field up these fields, NEVER EVER SHARE YOUR CONFIG FILE!
## ========================
class AuthConfig(object):
    s1_username = "darren.chan@csintelligence.asia"
    s1_password = "!k+t&3UZ2L5FQP2h"
    pov_username = "peepee"
    pov_password = "poopoo"
    srkk_username = "peepee"
    srkk_password = "poopoo"

    
    #pov_totp_secret = "H52U 6JTB GBWS CKCA IVJU 4WST HAXU QURK NR2H CPRD MJAS QJCT MF5A"
    #s1_totp_secret = "M5SEWYKNPU7CUVBTOAYW4UTTKZ3EMUJWFFTCCTCYGZBVCXLMGRUQ"

    haas_username = "soc1@reaqta.com"
    eurokars_password = "<Rbj=<E$p&#@25!FLx15x"
    msi_password = "FE&kuOkc!lwNU&6F0jg&wlxlsx"

## ========================
## Application-specific Settings:
## ------------------------
## ========================