import time
import sys
import random
import datetime
import telepot
import RPi.GPIO as GPIO
RELAY1=20
RELAY2=16
FAN=RELAY1
LIGHT=RELAY2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(RELAY1,GPIO.OUT)
GPIO.setup(RELAY2,GPIO.OUT)
TBTOKEN="your token"

def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return "On"

def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return "Off"

def handle(msg):
    chat_id=msg["chat"]["id"]
    print(str(chat_id))
    command=str(msg["text"])
    print "Received message from telegram %s% command"
    if "Fan" in command or "fan" in command:
        if "on" in command:
            bot.sendMessage(chat_id,str("Fan"+on(FAN)))
        elif "off" in command:
            bot.sendMessage(chat_id,str("Fan"+off(FAN)))
    elif "Light" in command or "light" in command:
        if "on" in command:
            bot.sendMessage(chat_id,str("Light"+on(LIGHT)))
        elif "off" in command:
            bot.sendMessage(chat_id,str("Light"+off(LIGHT)))
bot=telepot.Bot(TBTOKEN)
bot.message_loop(handle)
print "i am listening .. . .."

while 1:
    time.sleep(10)


