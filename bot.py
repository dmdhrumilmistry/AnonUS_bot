from flask import Flask, request
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import telebot
import validators 
import requests
import os

app_url = "https://anonus.herokuapp.com/"

server = Flask(__name__)

TOKEN = "<telegram-bot-api-token>"
bot = telebot.TeleBot(TOKEN)
start_message = '''
Welcome User, this bot and AnonUS (Anonymous URL shortner) are completely anonymous, it doesn't store any of your personal information, and we respect user privacy.
You can send link to this bot to generate short url.

The AnonUS is an Open source project, Any ideas or commits will be welcomed.
visit https://github.com/dmdhrumilmistry/AnonUS to create an issue.
'''


@bot.message_handler(commands=['start'])
def start(message):
    '''
    print start message and provide user option to generate new short link
    '''
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("/new_link"))

    response = bot.reply_to(message=message, text=start_message, reply_markup=markup)


@bot.message_handler(commands=["new_link"])
def new_link(message):
    markup = types.ForceReply(selective=False)
    response = bot.send_message(message.chat.id, "Enter Link and press send button ", reply_markup=markup)
    bot.register_next_step_handler(response, markup_handler)


def markup_handler(message):
    url = message.text
    if validators.url(url):
        request_url = app_url + "/new_link"
        app_response:dict = requests.post(
            request_url,
            headers={"Content-Type":"application/json"},
            json={"link":url}
        ).json()

        reply_message = ""
        for key in app_response:
            reply_message += f"{key} : {app_response[key]}"
        bot.reply_to(message, reply_message)
    
    else:
        bot.reply_to(message, "Invalid link")


# use below line while not using flask
# bot.infinity_polling()


# conf for heroku app using telegram webhook
@server.route('/'+TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode('utf-8'))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://app-name.herokuapp.com/'+TOKEN)
    return "!", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT',5000)))