import telebot
import os
from flask import Flask, request

# Telegram Bot Token
API_TOKEN = '8532724208:AAEe7dgO4iIijoptLJtprvhU7K_txg8Firo'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    msg = "🌟 VICA System အဆင်သင့်ဖြစ်ပါပြီ!\n\n/create [topic] ဟုရိုက်၍ AI ကို အလုပ်စခိုင်းနိုင်ပါသည်။"
    bot.reply_to(message, msg)

# Create Command
@bot.message_handler(commands=['create'])
def create_content(message):
    topic = message.text.replace('/create', '').strip()
    if not topic:
        bot.reply_to(message, "⚠️ Topic တစ်ခုခုထည့်ပေးပါ။ ဥပမာ- /create luxury_garage")
        return
    bot.reply_to(message, f"🚀 '{topic}' အတွက် Viral Content များ စတင်ဖန်တီးနေပါပြီ...")

# Web Server for Render
@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    return "VICA BOT IS ALIVE", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
