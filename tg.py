import telebot
from telebot import types
from datetime import datetime

token = 'your_token'
ADMIN_CHAT_ID = 'your_tg_admin_id'
bot = telebot.TeleBot(token)

active_chats = {}  # Словарь для отслеживания активных диалогов

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    btn3 = types.KeyboardButton('🇷🇸 Српски')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language / 🇷🇸 Изабери језик", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Изменить язык' or message.text == 'Change Language' or message.text == 'Промените језик':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🇷🇺 Русский")
        btn2 = types.KeyboardButton('🇬🇧 English')
        btn3 = types.KeyboardButton('🇷🇸 Српски')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language / 🇷🇸 Изабери језик", reply_markup=markup)
    elif message.text == '🇷🇺 Русский':  # rus
        send_russian_main_menu(message)
    elif message.text == '🇬🇧 English':  # eng
        send_english_main_menu(message)
    elif message.text == '🇷🇸 Српски':  # srb
        send_serbian_main_menu(message)
    elif message.text == 'Кто мы такие':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Мы - MakeACake Studios, молодая студия недавно появившаяся практически из ниоткуда. Наш создатель - Великий и Могучий @nalart11, он в принципе руководит всем происходящим здесь.", reply_markup=markup)
    elif message.text == 'Партнёрство':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Для связи с нами вы можете использовать один из нижеперечисленных способов:')
        bot.send_message(message.from_user.id, '[Наш Discord канал](https://discord.com/invite/uKXcU3py3q)', parse_mode='MarkdownV2')
        bot.send_message(message.from_user.id, 'Наш ТГ канал (Временно недоступен)')
        bot.send_message(message.from_user.id, '[ТГ владельца](https://t.me/nalart11)', parse_mode='MarkdownV2', reply_markup=markup)
    elif message.text == 'Как к нам попасть':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Назад')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Никак. 💀', reply_markup=markup)
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Кто мы такие')
        btn2 = types.KeyboardButton('Партнёрство')
        btn3 = types.KeyboardButton('Как к нам попасть')
        btn4 = types.KeyboardButton('Изменить язык')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)
    elif message.text == 'Who are we':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "We are MakeACake Studios, a young studio that recently appeared almost out of nowhere. Our creator is the Great and Powerful @nalart11, he basically directs everything that happens here.", reply_markup=markup)
    elif message.text == 'Partnership':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'To contact us you can use one of the following methods:')
        bot.send_message(message.from_user.id, '[Our Discord channel](https://discord.com/invite/uKXcU3py3q)', parse_mode='MarkdownV2')
        bot.send_message(message.from_user.id, 'Our Telegramm channel (Temporarily unavailable)')
        bot.send_message(message.from_user.id, "[Owner's Telegramm](https://t.me/nalart11)", parse_mode='MarkdownV2', reply_markup=markup)
    elif message.text == 'How to get to us':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Back')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'No way. 💀', reply_markup=markup)
    elif message.text == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Who are we')
        btn2 = types.KeyboardButton('Partnership')
        btn3 = types.KeyboardButton('How to get to us')
        btn4 = types.KeyboardButton('Change Language')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Ask a question', reply_markup=markup)
    elif message.text == 'Ко смо':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Повратак')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ми смо MakeACake Studios, млади студио који се недавно појавио готово ниоткуда. Наш креатор је Велики и Моћни @nalart11, он у суштини режира све што се овде дешава.", reply_markup=markup)
    elif message.text == 'Партнерство':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Повратак')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Да бисте нас контактирали, можете користити један од следећих метода:')
        bot.send_message(message.from_user.id, '[Наш Discord канал](https://discord.com/invite/uKXcU3py3q)', parse_mode='MarkdownV2')
        bot.send_message(message.from_user.id, 'Наш Telegramm канал (Привремено недоступан)')
        bot.send_message(message.from_user.id, "[Telegramm за креаторе](https://t.me/nalart11)", parse_mode='MarkdownV2', reply_markup=markup)
    elif message.text == 'Како доћи до нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Повратак')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Не долази у обзир. 💀', reply_markup=markup)
    elif message.text == 'Повратак':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ко смо')
        btn2 = types.KeyboardButton('Партнерство')
        btn3 = types.KeyboardButton('Како доћи до нас')
        btn4 = types.KeyboardButton('Промените језик')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Поставите питање', reply_markup=markup)
    elif message.text == 'Написать нам' or message.text == 'Contact us' or message.text == 'Контактирајте нас':
        start_dialog(message)
    elif message.text == 'Остановить диалог' or message.text == 'Stop dialog' or message.text == 'Зауставите дијалог':
        stop_dialog(message)
    elif message.from_user.id in active_chats:
        forward_message_to_admin(message)
    else:
        handle_non_command_message(message)

def send_russian_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Кто мы такие')
    btn2 = types.KeyboardButton('Партнёрство')
    btn3 = types.KeyboardButton('Как к нам попасть')
    btn4 = types.KeyboardButton('Изменить язык')
    btn5 = types.KeyboardButton('Написать нам')  # Новая кнопка для написания сообщения
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)

def send_english_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Who are we')
    btn2 = types.KeyboardButton('Partnership')
    btn3 = types.KeyboardButton('How to get to us')
    btn4 = types.KeyboardButton('Change Language')
    btn5 = types.KeyboardButton('Contact us')  # New button for sending message
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '❓ Ask a question', reply_markup=markup)

def send_serbian_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Ко смо')
    btn2 = types.KeyboardButton('Партнерство')
    btn3 = types.KeyboardButton('Како доћи до нас')
    btn4 = types.KeyboardButton('Промените језик')
    btn5 = types.KeyboardButton('Контактирајте нас')  # Нова дугмад за слање поруке
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.from_user.id, '❓ Поставите питање', reply_markup=markup)

def handle_non_command_message(message):
    bot.send_message(message.from_user.id, "Команда не распознана. Пожалуйста, выберите из доступных опций.")

def start_dialog(message):
    client_id = message.from_user.id
    username = message.from_user.username
    markup = types.InlineKeyboardMarkup()
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    active_chats[client_id] = {'username': username, 'start_time': start_time, 'messages': []}
    end_button = types.InlineKeyboardButton("Завершить диалог", callback_data=f"stop_{client_id}")
    markup.add(end_button)
    bot.send_message(message.from_user.id, "📝 Напишите ваше сообщение. Для завершения диалога нажмите 'Завершить диалог'.", reply_markup=markup)
    notify_admin_about_new_chat(client_id, username, start_time)

def forward_message_to_admin(message):
    client_id = message.from_user.id
    active_chats[client_id]['messages'].append(message.text)
    markup = types.InlineKeyboardMarkup()
    reply_button = types.InlineKeyboardButton("Ответить", callback_data=f"reply_{client_id}")
    end_button = types.InlineKeyboardButton("Завершить диалог", callback_data=f"end_{client_id}")  # Добавлена кнопка для завершения диалога
    markup.add(reply_button, end_button)
    bot.send_message(ADMIN_CHAT_ID, f"Сообщение от {active_chats[client_id]['username']} ({client_id}): {message.text}", reply_markup=markup)

def notify_admin_about_new_chat(client_id, username, start_time):
    bot.send_message(ADMIN_CHAT_ID, f"Новый диалог:\nTelegram ID: {client_id}\nUsername: @{username}\nВремя начала: {start_time}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("reply_") or call.data.startswith("end_") or call.data.startswith("stop_"))
def callback_handler(call):
    if call.data.startswith("reply_"):
        client_id = int(call.data.split("_")[1])
        if client_id in active_chats:
            bot.send_message(call.message.chat.id, f"Ответьте пользователю {client_id}:")
            bot.register_next_step_handler(call.message, process_admin_reply, client_id)
        else:
            bot.send_message(call.message.chat.id, "Диалог не найден. Проверьте правильность client_id.")
    elif call.data.startswith("end_"):
        client_id = int(call.data.split("_")[1])
        if client_id in active_chats:
            stop_dialog_by_admin(call, client_id)
        else:
            bot.send_message(call.message.chat.id, "Диалог не найден. Проверьте правильность client_id.")
    elif call.data.startswith("stop_"):
        client_id = int(call.data.split("_")[1])
        if client_id in active_chats:
            stop_dialog(client_id)
        else:
            bot.send_message(call.message.chat.id, "Диалог не найден. Проверьте правильность client_id.")


def process_admin_reply(message, client_id):
    response = message.text
    bot.send_message(client_id, f"Ответ: {response}")
    bot.send_message(message.chat.id, f"Ответ отправлен пользователю {client_id}: {response}")

def stop_dialog(client_id):
    if client_id in active_chats:
        bot.send_message(client_id, "Диалог завершен.")
        bot.send_message(ADMIN_CHAT_ID, f"Диалог с {active_chats[client_id]['username']} ({client_id}) завершен.")
        del active_chats[client_id]
    else:
        bot.send_message(client_id, "У вас нет активного диалога.")

def stop_dialog_by_admin(call, client_id):
    if client_id in active_chats:
        bot.send_message(client_id, "Диалог завершен администратором.")
        bot.send_message(call.message.chat.id, f"Диалог с {active_chats[client_id]['username']} ({client_id}) завершен.")
        del active_chats[client_id]
    else:
        bot.send_message(call.message.chat.id, "Диалог не найден.")

bot.infinity_polling(none_stop=True, interval=0)
