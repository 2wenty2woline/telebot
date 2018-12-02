# write bot telegram

import telebot
import constants

bot = telebot.TeleBot(constants.token)

# ===== Декораторы =====
@bot.message_handler(commands=['start'])
def hendle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start','/stop')
    user_markup.row('фото','аудио','документы')
    user_markup.row('стикер','видео','голос','локация')
    bot.send_message(message.from_user.id, 'Добро пожаловать в мой мир, человечек.', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def hendle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'Меня не остановить такой командой', reply_markup=hide_markup)

# ===== Декораторы =====

bot.polling(none_stop=True, interval=0)

