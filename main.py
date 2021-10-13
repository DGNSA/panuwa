import os
import telebot

bot=telebot.TeleBot("2091627071:AAHzgJf4S1i_UBGA2ciAcUJdxTuLj1R0cho")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"හායි, මමයි ඔයාලගෙ පණුවා")

@bot.message_handler(commands=["hello"])
def send_message(message):
    bot.send_message(message,"මොන හොදින් ද අනෙ. ඇදිරිනීතිය නිසා කොලයක්වත් කන්න බැ ගනන් වැඩි")

@bot.message_handler(commands=["help"])
def send_message(message):
    bot.send_message(message,"උදව්වක් විදිහට මට පුලුවන් ඔයාගෙ ගෙදර මල් ගස්වල කොල කන්න")

@bot.message_handler(commands=["panuwa"])
def send_message(message):
    bot.send_message(message,"ඒ මගෙ නම.ඇයි මගෙ නම පාඩම් කරනවාද")

@bot.message_handler(commands=["command"])
def send_message(message):
    bot.send_message(message,"start,hello,help,panuwa,command")

bot.polling()
