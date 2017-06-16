#!/usr/bin/env python3
# python-telegram-bot https://python-telegram-bot.org/
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging
import operator
from calc import calcip

updater = Updater(token='TOKEN')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, I can calculate range of IPs for subnets!") # Welcome message

# Function that validates operation introduced and print the result
def op(bot, update):
    hosts, net_address = update.message.text.split(",")
    h, r = calcip(hosts, net_address)
    h = "Netmask: " + h
    r = "Range: " + r
    bot.send_message(chat_id=update.message.chat_id, text=h)
    bot.send_message(chat_id=update.message.chat_id, text=r)

start_handler = CommandHandler('start', start)
op_handler = MessageHandler(Filters.text, op)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(op_handler)

updater.start_polling()
