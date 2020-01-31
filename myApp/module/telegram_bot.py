import telegram

myId = '700562335'
myToken = '1051923649:AAFHlrYs0GkO4OOOVunYFXFpiKKjFx0g34I'

bot = telegram.Bot(token=myToken)
print('hi')
# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id=myId, text='test message by DJango')