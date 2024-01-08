# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request
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
    global tempTextList
    while True:
        try:
            f = open('data.txt','r')
            s = ''
            for line in f:
                s+=line
            orders = []
            if s not in tempTextList:
                tempTextList.append(s)
                for ix in s.split('#'):
                    orders.append(ix)
                
                for order in orders:
                    if order not in text_list:
                        text_list.append(order)
                        all_data.append([datetime.now().strftime("%d/%m/%Y %H:%M:%S"), order])
                print(all_data)
                f.close()
        except:
            print('Error!!')

@app.route('/store_values', methods=['GET'])
def store_values():
    # Retrieve values from the GET request
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')

    # Do something with the values (e.g., store them in a database)
    # For demonstration purposes, print them to the console
    hadgeDict[str(value1)] = str(value2)
    print((f"Value 1: {value1}, Value 2: {value2}"))

    # You can also return a response if needed
    return "Values stored successfully!"



# main driver function
if __name__ == '__main__':
    all_data = [ ]
    text_list = []
    tempTextList = []
    hadgeDict = []
    thread = Thread(target = read_file)
    thread.start()
    # app.run(host= "199.247.31.183" , port="80")
    app.run(host='0.0.0.0' , port='80')
    
	
