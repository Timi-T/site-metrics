#!/usr/bin/python3
"""
Query all teh sites to get metrics
"""

from datetime import datetime
import json
from time import sleep
import requests
import base64

reset = 0

while True:
    """ ============= Project 1 =============== """
    #Query producktiv frontend || Method: GET

    prod_front = requests.get('https://producktiv.onrender.com')
    payload1 = {}
    payload1["Project name"] = "Producktiv frontend"
    payload1["Time"] = str(datetime.now())
    payload1["status"] = prod_front.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload1)
        json.dump({"logs": new_logs}, f, indent=4)

    #Query producktiv backend || Method: POST
    login_info = str(base64.b64encode('ope@gmail.com:opeyemi@kuz'.encode("ascii")))
    login_info = 'Basic ' + (login_info.split("'"))[1]
    prod_back = requests.post('https://producktiv-backend.onrender.com/api/login', headers={ "authorization": login_info })
    payload2 = {}
    payload2["Project name"] = "Producktiv backend"
    payload2["Time"] = str(datetime.now())
    payload2["status"] = prod_back.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload2)
        json.dump({"logs": new_logs}, f, indent=4)
    """ ============= END =============== """

    """ ============= Project 2 =============== """
    #Query fees-manager frontend || Method: GET

    fees_man = requests.get('https://fees-manager.onrender.com')
    payload3 = {}
    payload3["Project name"] = "Fees-manager frontend"
    payload3["Time"] = str(datetime.now())
    payload3["status"] = fees_man.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload3)
        json.dump({"logs": new_logs}, f, indent=4)

    """ ============= END =============== """

    """ ============= Project 3 =============== """
    #Query schfees-manager || Method: GET

    schfees_man = requests.get('https://schfees-manager.onrender.com')
    payload4 = {}
    payload4["Project name"] = "Schfees-manager"
    payload4["Time"] = str(datetime.now())
    payload4["status"] = schfees_man.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload4)
        json.dump({"logs": new_logs}, f, indent=4)

    """ ============= END =============== """

    """ ============= Project 4 ===============
    #Query AirBnB || Method: GET

    airbnb = requests.get('https://hbnb.onrender.com')
    payload5 = {}
    payload5["Project name"] = "AirBnB"
    payload5["Time"] = str(datetime.now())
    payload5["status"] = airbnb.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload5)
        json.dump({"logs": new_logs}, f, indent=4)

     ============= END =============== """

    """ ============= Project 5 =============== """
    #Query portfolio || Method: GET

    portforlio = requests.get('https://ogunbode-portfolio.onrender.com/')
    payload6 = {}
    payload6["Project name"] = "portfolio project"
    payload6["Time"] = str(datetime.now())
    payload6["status"] = portforlio.status_code
    with open("logs", "r") as f:
        old_logs_json = json.load(f)
    with open("logs", "w") as f:
        new_logs = old_logs_json.get('logs')
        if not new_logs:
            new_logs = []
        new_logs.append(payload6)
        json.dump({"logs": new_logs}, f, indent=4)

    """ * ============= END =============== """

    sleep(180)
    reset += 60
    if reset == (60 * 60 * 2):
        reset = 0
        with open("logs", "w") as f:
            json.dump({"logs": []}, f, indent=4)
