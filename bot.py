import telebot
import tok

bot = telebot.TeleBot(tok.token)

@bot.message_handler(content_types=["text"])
def all_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__== "__main__":
    bot.polling(non_stop=True)