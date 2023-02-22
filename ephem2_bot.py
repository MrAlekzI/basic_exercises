'''
Изменени:
1.Добавлена команда для получении информации о дате следующего полнолуния:
Реализуйте в боте команду, которая отвечает на вопрос “Когда ближайшее полнолуние?”
 Например /next_full_moon 2019-01-01. Чтобы узнать, когда ближайшее полнолуние, используйте ephem.next_full_moon(ДАТА)

2. убрана реализация выбора объекта класса через eval - заменено на getattr()
3. унифицировано форматирование дат при выводе сообщения пользователю
'''

import ephem
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import date, datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context):
    text = 'Вызван /start \n введите /planet объект ДД/MM/ГГГГ,\
    или только объект, если хотите узнать про сегодня \
    или введите /next_moon (ДАТА), чтобы узнать дату следующего полнолуния'
    print(text)
    update.message.reply_text(text)

# для нижеописанной функции если через date.today() то форматирование значения по умолчанию не работает в боте\
# , решил не связываться с престановкой вызваных атрибутов в f-string при return

def constellation (planet, user_date):
    try:
        planet_type = getattr(ephem, planet.capitalize())
        planet_time = planet_type(user_date)
        #planet_time = eval(f'ephem.{planet.capitalize()}("{user_date}")')
        #planet_time = onvertion = exec(f'ephem.{planet}("{date}")') #это почему то не работает
        return f'Планета {planet.capitalize()} на дату {user_date} проходит в созвездии {ephem.constellation(planet_time)[1]}'
    except (TypeError, AttributeError):
        return 'Вы выбрали не зодиакальный объект'
        
def user_moon(user_date):
    full_moon_date = ephem.next_full_moon(user_date)
    return f'Следующее полнолуние будет {full_moon_date}'

def user_request_const(update, context):
    user_text = update.message.text.split()
    print(user_text)
    if len(user_text) >= 3:
      user_date = user_text[2]
    elif len(user_text) == 2:
      user_date = datetime.now().strftime('%d/%m/%y')
    update.message.reply_text(constellation(user_text[1], user_date))

def user_request_moon(update, context):
    user_text = update.message.text.split()
    print(user_text)
    if len(user_text) == 2:
      user_date = user_text[2]
    elif len(user_text) == 1:
      user_date = datetime.now().strftime('%d/%m/%y')
    update.message.reply_text(user_moon(user_date))




def main():
    mybot = Updater(settings.TOKEN_ephem, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", user_request_const))
    dp.add_handler(CommandHandler("next_moon", user_request_moon))
    dp.add_handler(MessageHandler(Filters.text, user_request_const))
    dp.add_handler(MessageHandler(Filters.text, user_request_moon))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()