# -*- coding: utf-8 -*-
# IMPORTS COMECAM AQUI
import requests
import telepot
import time
# IMPORTS ACABAM AQUI
telepot == 9.1
requests == 2.11
# CORZINHA DE GAY COMECA AQUI
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'
#CORZINHA DE GAY ACABA AQUI


def handle(msg):
    tipomsg, tipochat, chat_id = telepot.glance(msg)
    if 'text' not in msg:
        print(f'''[{G}i{RT}] Uma Mensagem Que Nao E Um Texto Foi Recebida''')
        return
    command = msg['text'].split(' ')
    if command[0] == '/menu':  # COMANDO AQUI
        bot.sendMessage(chat_id, 'Texto Aqui')


bot = telepot.Bot('1545992060:AAG1J8PGH_EmSFaviXJ_Cy97dp56yNTD1fc')  # YOUR TOKEN HERE
bot.message_loop(handle)
print(f'[{G}+{RT}]ON...')

while 1:
    time.sleep(10)
