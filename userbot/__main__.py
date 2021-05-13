# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """
import platform
import shutil
import sys
import pip
import distro
import time
import os
import re
import time
from importlib import import_module
from sys import argv
from telethon import TelegramClient, events, Button
import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import LOGS, bot, BOT_TOKEN, BOT_USERNAME, API_KEY, API_HASH, ALIVE_LOGO, USERBOT_VERSION, StartTime, ALIVE_NAME, CMD_HELP
from userbot.modules import ALL_MODULES
from platform import python_version, uname
from shutil import which
import psutil
from git import Repo
from telethon import __version__, version


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'


try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)
    
    
try:
    LOGS.info("Initiating InlineBot....")
    inlinebot = TelegramClient("inlinebot", API_KEY, API_HASH).start(bot_token=BOT_TOKEN)
    bot.loop.run_until_complete(add_bot(BOT_USERNAME))
    LOGS.info("InlineBot is online now")
except Exception as e:
    LOGS.info("InlineBot Failed .")
    LOGS.info("InlineBot is quiting...")
    LOGS.info(str(e))
    
LOGS.info("You are running Project Fizilion")

LOGS.info(
    "Congratulations, your userbot is now running !! Test it by typing .alive / .on in any chat."
    "If you need assistance, head to https://t.me/ProjectFizilionChat")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
