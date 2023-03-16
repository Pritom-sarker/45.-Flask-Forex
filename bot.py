from telethon import TelegramClient, events
import time

def writeText(textt):
    print(textt)
    s = ''
    for t in textt[-5:]:
        s+=str(t)+'#'
        
    # while True:
        # try:
    f = open('data.txt', 'w')
    f.write(s)
    f.close()
        #     break
        # except:
        #     time.sleep(1)
        #     pass

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
            
            lines =  s.split('\n')
            for line in lines:
                if "ORDER".lower() in line.lower():
                    s = line
                    oldText.append(s)
                    print(s)
                    print(oldText)
                    break
            if 'ORDER'.lower() in s.lower():
                writeText(oldText)
                print('write!!!')
            else:
                print('Ignored!!!')
        print('----------------------')

if __name__ == '__main__':
    
    oldText = []
    for i in range(0,5):
        oldText.append(i)
    id = '21000478'
    hash = "fb9ec891a5dfefb02c0b41d78029d5a2"
    telApiName = 'ms'
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
