import os
import telebot
import random

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)


bot.set_my_commands([
    telebot.types.BotCommand("/start", "Get started"),
    telebot.types.BotCommand("/help", "Need some help?"),
    telebot.types.BotCommand("/vip", "Vip purchase"),
    telebot.types.BotCommand("/subscribe", "Subscribe"),
    telebot.types.BotCommand("/luckydraw", "Take a part in LuckyDraw"),
])

@bot.message_handler(commands=["start"])
def hello(message):
  bot.send_message(message.chat.id, "Hi Iam BetX Bot. if you press /help button you will get some commands for help.")

@bot.message_handler(commands=["help"])
def help(message):
  bot.send_message(message.chat.id,"Subscribe to VVIP to get access to the games 💥💰💰 99% winning Record.\nPress /h for advance help.\nPress /luckydraw for SATS Luckydraw 💰")

@bot.message_handler(commands=["vip"])
def vip(message):
  bot.send_message(message.chat.id,"💥 Press @BETNEPAL56 for the VIP Purchase of Betslip")

@bot.message_handler(commands=["subscribe"])
def subscribe(message):
  bot.send_message(message.chat.id,"Press https://t.me/BetXtreme_prediction to subscribe our free bets ❤")

@bot.message_handler(commands=["luckydraw"])
def luckydraw(message):
  luckynum = random.randint(1,5)
  msg = ( "🎉 Congrats you WON " + str(luckynum) + " SATS")
  bot.send_message(message.chat.id,msg)


bot.polling()
