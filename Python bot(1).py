from telegram import *
from telegram.ext import *


bot = Bot("<Your api>")
#print(bot.get_me())

updater=Updater("1498479585:AAEBSVUjShyfUcXZvFuxkGtd4qjl44HLodI",use_context=True)

dispatcher=updater.dispatcher

def function_1(update:Update,context:CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="<text>"
		)


start_value=CommandHandler('<command>',test_function)

dispatcher.add_handler(start_value)


def test_function1(update:Update,context:CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="<text>",
		)


start_value1=CommandHandler('<command>',test_function1)

dispatcher.add_handler(start_value1)

def test_function2(update:Update,context:CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="<text>",
		)


start_value2=CommandHandler('<command>',test_function2)

dispatcher.add_handler(start_value2)

updater.start_polling()
