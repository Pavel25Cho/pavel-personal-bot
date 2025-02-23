import os, schedule, asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest

maxBioLength = 140
defaultBio = os.environ.get('TELEGRAM_BIO')
client = TelegramClient('anon', os.environ.get('TELEGRAM_APP_ID'), os.environ.get('TELEGRAM_APP_HASH'))
    
def getDefaultBioLength():
    return len(defaultBio)    

async def updateBio(bio = '', keepDefault = True):
    if not client.is_connected():
        print("Client not connected.  Not updating bio.")
        return
    
    print('Updating bio...')
    newBio = (defaultBio if keepDefault else '') + ' '
    
    availableLength = maxBioLength - len(newBio)
    
    newBio = newBio + str(bio)[:availableLength]
    
    try:
        await client(UpdateProfileRequest(about = newBio[:maxBioLength]))
        print("Bio updated successfully.")
    except Exception as e:
        print(f"Error updating bio: {e}")
        

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
        
    # if '!updateBio' in event.raw_text:
        # await event.reply('hi!')
        # await changeBio('Проверка апишки')
        # os.environ['TELEGRAM_BIO1'] = 'test'
        # print(event)

async def schedule_task():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)
        
async def main():
    schedule.every(2).minutes.do(lambda: asyncio.create_task(updateBio()))

    await schedule_task()

with client:
    client.start()
    client.loop.run_until_complete(main())