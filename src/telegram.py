import os, datetime, schedule, time, asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest


defaultBio = os.environ.get('TELEGRAM_BIO')
client = TelegramClient('anon', os.environ.get('TELEGRAM_APP_ID'), os.environ.get('TELEGRAM_APP_HASH'))
    
def updateBio(bio = '', keepDefault = True):
    if client.is_connected() == False:
        return
    
    newBio = (defaultBio if keepDefault else '') + ' ' + str(bio)
    
    client(UpdateProfileRequest(
        about = newBio[:140]
    ))

@client.on(events.NewMessage)
async def my_event_handler(event):
    sender = await event.get_sender()
    me = await client.get_me()
    
    if sender != me:
        return
    
    if '!status' in event.raw_text:
        telegramConnected = client.is_connected()
        spotifyConnected = False
        
        await event.reply('Telegram status: ' + str(telegramConnected) + '\nSpotify status: ' + str(spotifyConnected))
        
        # await changeBio('Провекра апишки')
        
    # if '!updateBio' in event.raw_text:
        # await event.reply('hi!')
        # await changeBio('Проверка апишки')
        # os.environ['TELEGRAM_BIO1'] = 'test'
        # print(event)


# schedule.every(1).minutes.do(updateBio(datetime.datetime.now()))
# schedule.run_pending()

client.start()
client.run_until_disconnected()