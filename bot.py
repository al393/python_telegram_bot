# -*- coding: utf-8 -*-
import logging
import settings
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Подключаем логгирование по уровню 'INFO' с выводом в файл bot.log
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def start_bot(update: Updater, context: CallbackContext):
    with open('text_update.txt', 'a', encoding='utf-8') as file:
        print(update, end='\n', file=file)

    mytext = """Hello {}

    I have only /start command! ))""".format(update.message.chat.first_name)
    update.message.reply_text(mytext)


def chat(update: Updater, context: CallbackContext):
    text = f"user {update.message.chat.first_name}/id {update.message.chat.id}/ say: {update.message.text}"
    logging.info(text)
    update.message.reply_text(text)


def main():
    logging.info('Bot started!')
    updtr = Updater(settings.TOKEN_TELEGRAM)

    updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()


if __name__ == "__main__":
    main()