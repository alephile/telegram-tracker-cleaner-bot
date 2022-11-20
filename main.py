import logging
from telegram import Update
from telegram.ext import Application, filters, MessageHandler, CallbackContext


async def trimmer(update: Update, context: CallbackContext):
    str = update.message.text
    if str.startswith('https://twitter.com/') and str.find('t=') != -1:
        str = str.split('?')[0]
        await context.bot.send_message(chat_id = update.effective_chat.id, text = str)
    print(str)

if __name__ == '__main__':
    token = ''

    application = Application.builder().token(token).build()

    msg_handler = MessageHandler(filters.TEXT, trimmer)
    application.add_handler(msg_handler)

    application.run_polling()

    
