ConsultBot (Найти в телеграме можно как @Consult22Bot)
Бот для расписания пар на языке Python для Telegram
Бот создан для того, чтобы студент мог в любое время зайти в телеграм,
с помощью своего смартфона, и нажатием одной кнопки в чате с Ботом
узнать расписание занятий за определённый день.

Как компилятор, я использовал PyCharm
(Можете скачать по ссылке https://www.jetbrains.com/ru-ru/pycharm/)

Для создания бота, сначала вам нужно зайти в чат @BotFather в самом телеграме
Создание там очень простое, просто читайте и делайте как написано
После этого @BotFather напишет сообщение с Токеном вашего бота, который нужно будет вставить в эту строку в коде -

bot = telebot.TeleBot('ЗАМЕНИТЬ ЭТОТ ТЕКСТ НА ТОКЕН НЕ УБИРАЯ КАВЫЧКИ')

Изменение кода под своё расписание максимально простое.
Для этого используйте комментарии в коде(Справа от кода на 18 и 28 строке)

Для переноса Бота на сервер, я использовал сервис Heroku(Бесплатный)
Очень простой 9 минутный гайд по переносу бота -
https://www.youtube.com/watch?v=B72-sZyiW10&ab_channel=%D0%92%D0%BB%D0%B0%D0%B4%D0%9D%D0%B5%D0%B2%D0%B5%D1%80%D0%BE%D0%B2

