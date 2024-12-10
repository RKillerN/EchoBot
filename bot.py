from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN

def start(update, context):
    update.message.reply_text('¡Hola! Soy un bot de eco.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
