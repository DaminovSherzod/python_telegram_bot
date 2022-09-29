import telegram 
import os 
TOKEN = os.environ['TOKEN']
bot = telegram.Bot(token=TOKEN)
chat_id = '1219709167'
user = bot.getMe()
def KeyboardButton():
    button = {
        'text':'button1'
    }
    button1 = {
        'text':'button2'
        }
    keyboar = [
        [button],[button1]
    ]
    reply_markup = {
        'keyboard':keyboar
    }
    return reply_markup
def sendMessage(chat_id:'1219709167', text:str,reply_markup=KeyboardButton()):
    send = bot.sendMessage(chat_id,text,reply_markup)
    return send
def getUpdate():
    update = bot.getUpdates()
    result = update[-1]
    text = result.message.text
    chat_id = result.message.chat.id
    update_id = result.update_id
    return text,chat_id,update_id


print(sendMessage(text='hello'))














# last_update_id = getUpdate()[-1]
# current_update_id = -1

# while True:
#     result = 0
#     current_update_id = getUpdate()[-1]
#     if last_update_id !=current_update_id:
#         text, chat_id, current_update_id = getUpdate()
#         sendMessage(chat_id, text)
#         last_update_id = current_update_id

