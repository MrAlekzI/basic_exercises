'''
Реализуйте в боте команду /wordcount которая считает слова в присланной фразе. Например на запрос /wordcount Привет как дела бот должен ответить: 3 слова. Не забудьте:

Добавить проверки на пустую строку
Как можно обмануть бота, какие еще проверки нужны?
'''
import re
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Введите /wordcount b напишите какую-нибудь фразу, а я посчитаю колличество слов в ней'
    print(text)
    update.message.reply_text(text)

#проверки - числа, знаки препинаия, разденеие знаками препинания без пробела
def text_check (text):
    pattern = r'[\d\W_]+'  
    new_text = re.sub(pattern, ' ', text) #далее удаляем альтернативные разделители вместо пробела
    return new_text

def user_request(update, context):
    user_text = text_check(update.message.text[10:])
    print(user_text)
    txt = user_text.split()
    if len(txt) == 0:
        update.message.reply_text('Вы ввели пустую строку') #проверка на пустую строку
    else:
        update.message.reply_text(f'Количсетво слов в строке: {len(txt)}')



def main():
    mybot = Updater(settings.TOKEN_wordcount, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('wordcount', user_request))
    dp.add_handler(MessageHandler(Filters.text, user_request))
 
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()