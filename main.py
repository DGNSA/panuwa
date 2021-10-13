import os
import telebot
import pytube

bot=telebot.TeleBot("2091627071:AAHzgJf4S1i_UBGA2ciAcUJdxTuLj1R0cho")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"හායි, මමයි ඔයාලගෙ පණුවා")

@bot.message_handler(commands=["hello"])
def send_message(message):
    bot.reply_to(message,"මොන හොදින් ද අනෙ. ඇදිරිනීතිය නිසා කොලයක්වත් කන්න බැ ගනන් වැඩි")

@bot.message_handler(commands=["help"])
def send_message(message):
    bot.reply_to(message,"උදව්වක් විදිහට මට පුලුවන් ඔයාගෙ ගෙදර මල් ගස්වල කොල කන්න")

@bot.message_handler(commands=["panuwa"])
def send_message(message):
    bot.reply_to(message,"ඒ මගෙ නම.ඇයි මගෙ නම පාඩම් කරනවාද")

@bot.message_handler(commands=["ytdownload"])
def send_message(message):
    bot.reply_to(message,"Downloading")
    bot.reply_to(message,x=input("Enter Your Link :"))
    url = x
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video = youtube.streams.get_lowest_resolution()
    bot.send_video(video)
    bot.reply_to(message,"Download Succesfull!")

bot.polling()
