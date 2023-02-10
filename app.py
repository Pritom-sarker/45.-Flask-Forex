# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from telethon import TelegramClient, events
import threading


app = Flask(__name__)
 
 
 
 
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    f = open('data.txt','r')
    s = ''
    for line in f:
        s+=line
    f.close()
    return s

    
# main driver function
if __name__ == '__main__':
    app.run(host= "199.247.31.183" , port="80")
    
	
