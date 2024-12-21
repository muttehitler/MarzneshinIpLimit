"""
Read config file and return data.
"""
# pylint: disable=global-statement

import json
import os
import sys
import time

CONFIG_DATA = None
LAST_READ_TIME = 0


async def read_config(
    check_required_elements=None,
) -> dict:
    """
    read and return data from a JSON file.
    """
    global CONFIG_DATA
    global LAST_READ_TIME
    config_file = "config.json"

    if not os.path.exists(config_file):
        print("Config file not found.")
        sys.exit()
    file_mod_time = os.path.getmtime(config_file)
    if CONFIG_DATA is None or file_mod_time > LAST_READ_TIME:
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                CONFIG_DATA = json.load(f)
        except json.JSONDecodeError as error:
            print(
                "Error decoding the config.json file. Please check its syntax.", error
            )
            sys.exit()
        if "BOT_TOKEN" not in CONFIG_DATA:
            print("BOT_TOKEN is not set in the config.json file.")
            sys.exit()
        if "ADMINS" not in CONFIG_DATA:
            print("ADMINS is not set in the config.json file.")
            sys.exit()
        LAST_READ_TIME = time.time()
    if check_required_elements:
        required_elements = [
            "PANEL_DOMAIN",
            "PANEL_USERNAME",
            "PANEL_PASSWORD",
            "CHECK_INTERVAL",
            "TIME_TO_ACTIVE_USERS",
            "IP_LOCATION",
            "GENERAL_LIMIT",
        ]
        for element in required_elements:
            if element not in CONFIG_DATA:
                raise ValueError(
                    f"Missing required element '{element}' in the config file."
                )
    return CONFIG_DATA


async def read_detected_users_config(
    check_required_elements=None,
) -> dict:
    """
    read and return data from a JSON file.
    """
    global CONFIG_DATA
    global LAST_READ_TIME
    config_file = "detected_users.json"

    if not os.path.exists(config_file):
        print("Config file not found.")
        sys.exit()
    file_mod_time = os.path.getmtime(config_file)
    if CONFIG_DATA is None or file_mod_time > LAST_READ_TIME:
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                CONFIG_DATA = json.load(f)
        except json.JSONDecodeError as error:
            print(
                "Error decoding the detected_users.json file. Please check its syntax.", error
            )
            sys.exit()
        if "BOT_TOKEN" not in CONFIG_DATA:
            print("BOT_TOKEN is not set in the detected_users.json file.")
            sys.exit()
        if "ADMINS" not in CONFIG_DATA:
            print("ADMINS is not set in the detected_users.json file.")
            sys.exit()
        LAST_READ_TIME = time.time()
    if check_required_elements:
        required_elements = [
            "detectedUsers"
        ]
        for element in required_elements:
            if element not in CONFIG_DATA:
                raise ValueError(
                    f"Missing required element '{element}' in the detected_users file."
                )
    return CONFIG_DATA

async def detect_user(detectedUser: str, ips:str) -> str | None:
    """
    Add a user to the exception list in the config file.
    If the config file does not exist, it creates one.
    """
    if os.path.exists("detected_users.json"):
        data = await read_d_json_file()
        users = data.get("detectedUsers", [])
        if len([y for y in users if y["user"] == detectedUser]) > 0:
            user = next((y for y in users if y["user"] == detectedUser), None)
            user["outOfLimitCount"] = int(user["outOfLimitCount"]) + 1
            data["detectedUsers"] = users
            with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return detectedUser
        else:
            users.append({ "user":detectedUser, ips:ips, "outOfLimitCount":1 })
            data["detectedUsers"] = users
            with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return detectedUser
    else:
        data = {"detectedUsers": [detectedUser]}
        with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return detectedUser
    return None

async def add_detected_user(detectedUser: str, ips:list) -> str | None:
    """
    Add a user to the exception list in the config file.
    If the config file does not exist, it creates one.
    """
    if os.path.exists("detected_users.json"):
        data = await read_d_json_file()
        users = data.get("detectedUsers", [])
        if len([y for y in users if y["user"] == detectedUser]) > 0:
            return detectedUser
        else:
            users.append({ "user":detectedUser, "ips":ips, "outOfLimitCount":1 })
            data["detectedUsers"] = users
            with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return detectedUser
    else:
        data = {"detectedUsers": [detectedUser]}
        with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return detectedUser
    return None

async def delete_detected_user(detectedUser: str) -> str | None:
    """
    Add a user to the exception list in the config file.
    If the config file does not exist, it creates one.
    """
    if os.path.exists("detected_users.json"):
        data = await read_d_json_file()
        users = data.get("detectedUsers", [])
        if len([y for y in users if y["user"] == detectedUser]) > 0:
            users.remove(next((y for y in users if y["user"] == detectedUser), None))
            data["detectedUsers"] = users
            with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            return detectedUser
    else:
        data = {"detectedUsers": [detectedUser]}
        with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return detectedUser
    return None


async def get_detected_users() -> None:
    if os.path.exists("detected_users.json"):
        data = await read_d_json_file()
        return data.get("detectedUsers", [])
    else:
        data = {"detectedUsers": []}
        with open("detected_users.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
        return None
    return None


async def read_d_json_file() -> dict:
    """
    Reads and returns the content of the config.json file.

    Returns:
        The content of the config.json file.
    """
    with open("detected_users.json", "r", encoding="utf-8") as f:
        return json.load(f)
