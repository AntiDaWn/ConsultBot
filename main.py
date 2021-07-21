import telebot
from telebot import types

bot = telebot.TeleBot('1942173736:AAGDE6piA5WbVdzPvcDTHWy9P8ezOQIJsq4')

@bot.message_handler(commands=["start"])
def startKBoard(message):
    bot.send_message(message.chat.id, "Вы хотите знать расписание?(Да/Нет)")

@bot.message_handler(content_types=['text'])
def Nedelya(message):
    if message.text == "Да":
        catalogKBoard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        Monday = types.KeyboardButton(text="Понедельник")
        Tuesday = types.KeyboardButton(text="Вторник")
        Wednesday = types.KeyboardButton(text="Среда")
        Thursday = types.KeyboardButton(text="Четверг")
        Friday = types.KeyboardButton(text="Пятница")                          #Здесь, отступив строку, можете добавить ещё один день недели(Субботу)
                                                                               #Для этого используйте например эту строку - Friday = types.KeyboardButton(text="Пятница")
                                                                               #Заменив Friday например на Saturday и текст в кавычках аналогично на "Суббота"
        catalogKBoard.add(Monday, Tuesday, Wednesday, Thursday, Friday)
        bot.send_message(message.chat.id, "Выберите день недели", reply_markup=catalogKBoard)
    else:
        if message.text == "Нет":
            bot.send_message(message.chat.id, "Тогда увидимся позже")
        else:
            if message.text == "Понедельник":
                bot.send_message(message.chat.id, "1: технологии защиты информации (л)")     # Здесь вам нужно очевидно заменить текст в кавычках
                bot.send_message(message.chat.id, "2: компьютерные сети (л)")                # на ваше расписание.
                bot.send_message(message.chat.id, "3: технологии защиты (пр)")               # !!! С помощью Ctrl+C/Ctrl+V добавляйте строки
            elif message.text == "Вторник":                                                  # если у вас больше пар на неделе
                bot.send_message(message.chat.id, "1: организация БД (пр)")                  # и не бойтесь удалять лишние строки если у вас пар меньше
                bot.send_message(message.chat.id, "2: организация БД (л)")                   # Текст внутри кавычек редактируйте на своё усмотрение
                bot.send_message(message.chat.id, "3: многочисленные методы (л)")
                bot.send_message(message.chat.id, "4: компьютерные сети (пр)")
                bot.send_message(message.chat.id, "5: многочисленные методы (пр)")
            elif message.text == "Среда":
                bot.send_message(message.chat.id, "1: мигалка нет пары/инструментальные средства управления проектами (пр)")
                bot.send_message(message.chat.id, "2: компьютерные сети (пр)")
                bot.send_message(message.chat.id, "3: методы и технологии инженерии по (л)")
            elif message.text == "Четверг":
                bot.send_message(message.chat.id, "1: мигалка инструментальные средства управления проектами (л)/ нет пары")
                bot.send_message(message.chat.id, "2: архитектура компьютеров (л)")
                bot.send_message(message.chat.id, "3: архитектура компьютеров (пр)")
                bot.send_message(message.chat.id, "4: методы и технологии инженерии по (пр)")
            elif message.text == "Пятница":
                bot.send_message(message.chat.id, "3: межфакультетская дисциплина")
            else:
                bot.send_message(message.chat.id, "Попробуйте ответить ещё раз")
if __name__ == '__main__':
    bot.infinity_polling()




