# -*- coding: utf-8 -*-
import urllib.request
import mysql.connector
from mysql.connector import errorcode
import requests
import json
import telepot
import random
import re
import sys
import time
import random
from subprocess import run
from os import system
from time import sleep
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

system('clear')
from random import choice
telepot == 9.1
requests == 2.11
json == 18.2
random == 9.6
re == 7.2
sys == 28.1
time == 15.3

def handle(msg):
    tipomsg, tipochat, chat_id = telepot.glance(msg)
    if 'text' not in msg:
        print(f'''[{G}i{RT}] Uma Mensagem Que Nao E Um Texto Foi Recebida''')
        return
    command = msg['text'].split(' ')
    if command[0] == '/menu2': # COMMAND HERE
       bot.sendMessage(chat_id, 'text here')
        
bot = telepot.Bot('')  # YOUR TOKEN HERE
bot.message_loop(handle)
print(f'[{Y}i{RT}]Aguarde...')
print(f'[{G}+{RT}]ON...')

while 1:
    time.sleep(10)
