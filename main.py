from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('5947044995:AAENKfNCHx6rvy7Hb_bk1SRWACiEYRomu2g')
dp = Dispatcher(bot)

# отслеживание команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()

    # добавляем кнопку, при нажатии на которую будет открываться веб-приложение
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='file:///C:/Users/Kirill/Documents/Python/Bots/web_apps_tg_bot/index.html')))

    # выводим сообщение пользователю
    await message.answer('Привет, мой друг!', reply_markup=markup)

executor.start_polling(dp)