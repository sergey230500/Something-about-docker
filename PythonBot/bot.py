import telebot
from telebot import types
import database
import io
from io import BytesIO
from PIL import Image
fio = ""
description = ""
photo = ""

def convert_image_to_blob(image_path, format='JPEG'):
    image = Image.open(BytesIO(image_path))
    blob = BytesIO()
    image.save(blob, format)
    return blob.getvalue()

def blob_to_image(blob):
    image = Image.open(BytesIO(blob))
    return image

bot = telebot.TeleBot('7126907810:AAG9BbmtMrRDuz77dPSWb93m8q-BntW0yD8')



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "/reg":
        bot.send_message(message.from_user.id, "Добрый день! Укажите ФИО нарушителя")
        bot.register_next_step_handler(message, get_fio)
    elif message.text == "/show":
        bot.send_message(message.from_user.id, "Фамилия?")
        bot.register_next_step_handler(message, get_record)
    else:
        bot.send_message(message.from_user.id, "Я не знаю, как на это реагировать, если вы хотите добавить запись о нарушении, напишите /reg")
def get_fio(message):
    global fio
    fio = message.text
    bot.send_message(message.from_user.id, "Укажите суть нарушения")
    bot.register_next_step_handler(message, get_description)

def get_description(message):
    global description
    description = message.text
    bot.send_message(message.from_user.id, "Приложите фото")   
    bot.register_next_step_handler(message, get_photo)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    global description
    global fio
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        global photo
        photo = convert_image_to_blob(downloaded_file)
        # database.databaseinsert(fio, description, photo)
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
