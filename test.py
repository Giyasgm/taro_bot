from aiogram import executor, types

from aiogram.dispatcher.filters import CommandStart

from aiogram.types import InputFile

from aiogram.dispatcher import FSMContext

from Baza import bot, dp, Testik

from Raschet import Formules

from Openimage import koloda

from Buttons import mainmenu, text1, text2

from Textkart import arkans


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n"
                         f"{text2}\n"
                         f"Если вы захотите перезапустить бота, в любой момент используйте команду /start")
    await bot.send_message(message.from_user.id, f"{text1}")
    await Testik.test1.set()


@dp.message_handler(state=Testik.test1)
async def datarozh(message: types.Message, state: FSMContext):
    global infa
    if message.text[2] == '.' and message.text[5] == '.' and len(message.text) == 10:
        otvet = message.text

        await state.update_data(test1=otvet)
        datass = await state.get_data()
        infa = datass.get('test1')
        await bot.send_message(message.from_user.id, "Выберите интересующее вас предсказание", reply_markup=mainmenu)

    elif message.text == 'С чем вы пришли в этот мир':
        chatid = message.from_user.id
        arkankart = InputFile(path_or_bytesio=f"{koloda[Formules(infa).day()]}")
        await dp.bot.send_photo(chat_id=chatid, photo=arkankart, caption=f'{arkans[Formules(infa).day()][0]}')

    elif message.text == 'Чему можете научиться':
        chatid = message.from_user.id
        arkankart = InputFile(path_or_bytesio=f"{koloda[Formules(infa).month()]}")
        await dp.bot.send_photo(chat_id=chatid, photo=arkankart, caption=f'{arkans[Formules(infa).month()][1]}')

    elif message.text == 'Чего достигните':
        chatid = message.from_user.id
        arkankart = InputFile(path_or_bytesio=f"{koloda[Formules(infa).year()]}")
        await dp.bot.send_photo(chat_id=chatid, photo=arkankart, caption=f'{arkans[Formules(infa).year()][2]}')

    elif message.text == 'Ваша Карта Оберег':
        chatid = message.from_user.id
        arkankart = InputFile(path_or_bytesio=f"{koloda[Formules(infa).alldata()]}")
        await dp.bot.send_photo(chat_id=chatid, photo=arkankart, caption=f'{arkans[Formules(infa).alldata()][3]}')

    elif message.text == 'Возврат к вводу даты (нажмите на - /start)':
        await state.finish()

    else:
        await bot.send_message(message.chat.id, f"Вы неправильно ввели дату рождения, попробуйте ещё раз")


executor.start_polling(dp)
