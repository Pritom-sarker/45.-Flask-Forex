# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request, render_template, session, redirect
from telethon import TelegramClient, events
from threading import Thread
from datetime import datetime
import pandas as pd


app = Flask(__name__)
 
@app.route('/hist')
def All_data():
    global all_data
    
    df = pd.DataFrame(all_data,columns=['Datetime','Text'])
    df = df.sort_values(by=['Datetime'], ascending=False)
    return df.to_html(header="true", table_id="table")



 
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    f = open('data.txt','r')
    s = ''
    for line in f:
        s+=line
    f.close()
    return s

def read_file():
    while True:
        try:
            f = open('data.txt','r')
            s = ''
            for line in f:
                s+=line
            if s not in text_list:
                text_list.append(s)
                all_data.append([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), s])
                print(all_data)
            f.close()
        except:
            print('Error!!')

# main driver function
if __name__ == '__main__':
    all_data = [ ]
    text_list = []
    thread = Thread(target = read_file)
    thread.start()
    app.run(host= "199.247.31.183" , port="80")
#     app.run(host='0.0.0.0' , port='80')
    
	
