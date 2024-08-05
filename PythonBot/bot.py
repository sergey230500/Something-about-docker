import telebot
from telebot import types
import database
import io
from io import BytesIO
from PIL import Image
fio = ""
description = ""
photo = ""
runbot = False

def convert_image_to_blob(image_path, format='JPEG'):
    image = Image.open(BytesIO(image_path))
    blob = BytesIO()
    image.save(blob, format)
    return blob.getvalue()

def blob_to_image(blob):
    image = Image.open(BytesIO(blob))
    return image

bot = telebot.TeleBot('7126907810:AAG9BbmtMrRDuz77dPSWb93m8q-BntW0yD8')

@bot.message_handler(commands=['start'])
def startChat(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btnreg = telebot.types.InlineKeyboardButton('Зарегистрировать нарушение', callback_data = 'reg')
    markup.add(btnreg)
    btnstop = telebot.types.InlineKeyboardButton('Отменить регистрацию', callback_data = 'stop')
    markup.add(btnstop)
    btnshow = telebot.types.InlineKeyboardButton(text ='Показать записи', callback_data = 'show')
    markup.add(btnshow)
    bot.send_message(message.chat.id, "Добрый день!", reply_markup=markup)
    

@bot.callback_query_handler(func=lambda call: call.data == "show")
def button_clicked(call):
    markup = telebot.types.InlineKeyboardMarkup()
    names = database.getnames()
    for name in names:
        btn = telebot.types.InlineKeyboardButton(text=name, callback_data=name)
        markup.add(btn)
    bot.send_message(call.message.chat.id, 'Выберите нарушителя', reply_markup=markup)

    


@bot.callback_query_handler(func=lambda call: call.data == "reg")
def button_clicked(call):
    global runbot
    runbot = True
    bot.send_message(call.message.chat.id, "Добрый день! Укажите ФИО нарушителя")
    bot.register_next_step_handler(call.message,get_fio)
    
@bot.callback_query_handler(func=lambda call: call.data == "stop")
def button_clicked(call):
    global runbot
    runbot = False
    bot.send_message(call.message.chat.id, "Регистрация отменена")
    startChat(call.message)
    


def get_fio(message):
    global fio, runbot
    if runbot:
        fio = message.text
        bot.send_message(message.from_user.id, "Укажите суть нарушения")
        bot.register_next_step_handler(message, get_description)

def get_description(message):
    global description, runbot
    if runbot:
        description = message.text
        bot.send_message(message.from_user.id, "Приложите фото")   
        bot.register_next_step_handler(message, get_photo)

@bot.message_handler(content_types=['photo'])

def get_photo(message):
    global description, runbot
    global fio
    if runbot:
        if message.content_type == 'photo':
            file_info = bot.get_file(message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            global photo
            photo = convert_image_to_blob(downloaded_file)
            database.databaseinsert(fio, description, photo)
            trytosent = blob_to_image(photo)
            bot.send_photo(message.from_user.id, trytosent, caption="Нарушитель: " + fio +"\nСуть нарушения: " + description)
            bot.send_message(message.from_user.id, "Запись внесена в базу данных. Чтобы посмотреть записи нарушений, необходимо пройти по ссылке: http://192.168.10.11:8001")
        else:
            bot.send_message(message.from_user.id, "Это не фото")
            bot.register_next_step_handler(message, get_photo)

def get_record(message):
    
    try:
        data = database.read_BLOB(message)
        photo = io.BytesIO(data[3])
        fio = data[1]
        description = data[2]
        bot.send_photo(message.from_user.id, photo, caption="Нарушитель: " + fio +"\nСуть нарушения: " + description)
    except:
        bot.send_message(message.from_user.id, "Запись не найдена")
bot.polling(none_stop=True, interval=0)
