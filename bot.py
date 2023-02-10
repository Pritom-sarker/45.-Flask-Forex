from telethon import TelegramClient, events
import time

def writeText(textt):
    print('')
    s = ''
    lines =  textt.split('\n')
    for line in lines:
        if "ORDER" in line:
            s = line
            print(s)
            break
        
    while True:
        try:
            f = open('data.txt', 'w')
            f.write(s)
            f.close()
            break
        except:
            time.sleep(1)
            pass

def get_message_from_telegram():
    global oldText
    our_chanel = 1201000242
    @client.on(events.NewMessage(chats=our_chanel))
    async def my_event_handler(event):
        s = event.raw_text
        print(s)
        if str(s) in oldText:
            print('Same text!!')
        else:
            oldText.append(s)
            if 'ORDER'.lower() in s.lower():
                time.sleep(3)
                writeText(s)
            else:
                print('Ignored!!!')
        print('----------------------')

if __name__ == '__main__':
    
    oldText = []
    id = '14631934'
    hash = "62c6c4263e06b6f800acc32c188f1d6f"
    telApiName = 'newApi11'
    hour = 10
    print('Bot wll sleep for next ',hour,"Hours")
    # time.s/r * 3600)
    print('bot is running!!')

    client = TelegramClient(telApiName, id, hash)
    # tel account
    while True:
        try:
            client.start()
            get_message_from_telegram()
            client.run_until_disconnected()
        except Exception as e:
            print('ERROR SO AGAIN!!!',e)