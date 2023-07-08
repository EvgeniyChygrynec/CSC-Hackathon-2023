import telebot
from ready_model import generate_answer

token = '5928516367:AAHWFuj-3xyB21QkU5-hU5ugfm10zD0PMgE'
# https://t.me/chatgpt_revenuegrid_bot link bot
question = None

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, 'Hello!')

    @bot.message_handler(content_types=["text"])
    def send_text(message):
        global question
        question = message.text
        print(question)

        answer = process_question(question)

        bot.send_message(message.chat.id, answer)

    def process_question(question):

        if question != None:
            return generate_answer(question)
        else:
            pass


    bot.polling()

telegram_bot(token)