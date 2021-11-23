import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parser import ParsAT
import threading

# Объект бота
bot = Bot(token="1147643880:AAFi5gJPjpNsOmz240w95RtxC9LCKfPAJ4M")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

data_dict = {}



@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = ["Логинимся", "Без Логина"]
    keyboard.add(*buttons)
    await message.answer('Парсер Autor today. Можем залогинится, можно попробовать спарсить без входа')
    await message.answer("Что делаем?", reply_markup=keyboard)


@dp.message_handler(Text(equals='Без Логина'))
async def log_off(message: types.Message):
    await message.answer('Введите ссылку')

@dp.message_handler(Text(equals='Логинимся'))
async def log_in(message: types.Message):
    data_dict[message.from_user.id] = {}
    await message.answer('Введите логин и пароль через пробел')


@dp.message_handler(Text(contains='http'))
async def parsing(message: types.Message):
    cur_page = ''
    url = message.text

    await message.answer('Начинаем парсинг, подождите')
    if data_dict:
        data = data_dict[message.from_user.id]
        parser = ParsAT(url, data['login'], data['password'])
        threading.Thread(target=parser.login).start()
        # parser.login()

    else:
        parser = ParsAT(url)
        threading.Thread(target=parser.get_text).start()
        # parser.get_text()
    while parser.pars:
        if cur_page == parser.cur_chapter:
            continue
        else:
            cur_page = parser.cur_chapter
            await message.answer(str(cur_page))

    await message.answer('Парсинг завершен')


    try:
        await message.reply_document(open(parser.name + '.txt', 'rb'))
    except:
        await message.answer('Парсинг не удался')


@dp.message_handler(Text(contains='@'))
async def parsing_login(message: types.Message):
    data = data_dict[message.from_user.id]
    data['login'] = message.text.split()[0]
    data['password'] = message.text.split()[1]
    print(data)
    await message.answer('Введите ссылку')





if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)