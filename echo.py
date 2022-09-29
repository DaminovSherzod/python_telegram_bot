from telegram.ext import Updater,MessageHandler,Filters,CallbackContext,CommandHandler
from telegram import Update

import os
TOKEN = os.environ['TOKEN']

updater = Updater(TOKEN)

def echo(update: Update, context: CallbackContext):
    txt = update.message.text
    Like = 0
    Dislike = 0
    if txt == '👍':
        Like+=1
    elif txt == '👎':
        Dislike+=1
    text1 = f'Like:{Like}\n, Dislike:{Dislike}'
    user_id = update.message.from_user.id
    bot = context.bot
    bot.sendMessage(user_id,text1)
    return

def start(update: Update, context: CallbackContext):
    txt = 'Like and Dislike'
    user_id = update.message.from_user.id
    bot = context.bot
    bot.sendMessage(user_id,txt)
    return

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👍,👎'),echo))

updater.start_polling()
updater.idle()