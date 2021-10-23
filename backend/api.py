from flask import Flask,request,jsonify
from flask import Response
from flask_socketio import SocketIO
from flask_cors import CORS
import json
import flask
import sqlite3
import collections

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')
get_All_command = "SELECT * FROM food_post f "

@app.route('/getAll', methods=['GET'])#跳出所有輪播訊息
def get_all():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    c = cursor.execute(get_All_command)
    a = c.fetchall()
    all = []
    get_datetime_command = "SELECT time('now', 'localtime');"
    timer = cursor.execute(get_datetime_command)
    t = timer.fetchall()
    current_hour = t[0][0][0:2]
    current_min = t[0][0][3:5]
    for i in a:
        flag = False
        flag2 = False
        hour = i[4][0:2]
        min = i[4][3:]
        left_amount = i[5]
        if (hour > current_hour) : flag = True
        elif ((hour == current_hour) and (min > current_min)) : flag = True
        if(left_amount>0):flag2 = True
        if(flag and flag2):
            d = collections.OrderedDict()
            d['id'] = i[0]
            d['name'] = i[1]
            d['item'] = i[2]
            d['location'] = i[3]
            d['time'] = i[4]
            d['left'] = i[5]
            d['max'] = i[6]
            d['comment'] = i[7]
            d['url'] = "https://da26-140-113-124-40.ngrok.io/detail/"+str(i[0])
            all.append(d)
    j = json.dumps(all)
    return j
@app.route('/getDetail', methods=['GET'])#跳出指定圖文訊息 用string name判斷
def get_Detail():
    id = request.values.get('id')
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    query_detail = get_All_command + "where f.id = " + id+";"
    c = cursor.execute(query_detail)
    a = c.fetchall()
    all=[]
    for i in a :
        d = collections.OrderedDict()
        d['id'] = i[0]
        d['name'] = i[1]
        d['item'] = i[2]
        d['location'] = i[3]
        d['time'] = i[4]
        d['left'] = i[5]
        d['max'] = i[6]
        d['comment'] = i[7]
        d['url'] = "https://da26-140-113-124-40.ngrok.io/detail/"+str(id)
        all.append(d)
    j = json.dumps(all)
    return j
    

@app.route('/addForm', methods=['POST']) 
def add_Form():
    request_data = request.get_json()
    name = request_data['name']  
    item = request_data['item'] 
    location = request_data['location'] 
    time = request_data['time'] 
    left = request_data['left'] 
    max = request_data['max']   
    comment = request_data['comment'] 
    url = "https://da26-140-113-124-40.ngrok.io/detail/"
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    query2 = "INSERT INTO food_post (name,item,location,time,left,max,comment,url) VALUES (" + "\"" + name + "\"," + "\"" + item +"\"," + "\"" + location + "\"," + "\"" +time+ "\"," + left + "," + max + ",\"" + comment +  "\",\"" +url+ "\"" +")"
    print(query2)
    c = cursor.execute(query2)
    connection.commit()

    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    get_id_command = "SELECT id FROM food_post f " + "where f.item =\"" + item + "\" AND f.location = \"" + location  + "\" AND f.left = " + left + " AND f.max = " + max + " AND f.comment = \"" + comment + "\";"
    get_id = cursor.execute(get_id_command)
    get_id = get_id.fetchall()
    get_id = get_id[0][0]
    return_url = "https://d76b-140-113-124-40.ngrok.io/detail/" + str(get_id)
    connection.commit()
    res = {}
    if(get_id):
        res['url'] = return_url
        res['mes'] = 'add form success'
        return json.dumps(res)
    else :
        res['url'] = "fail"
        res['mes'] = 'add form fail'
        return json.dumps(res)

@app.route('/reserve', methods=['POST'])
def reserve():
    request_data = request.get_json()
    id = request_data['id']
    amount = request_data['amount']
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    
    query = "SELECT * FROM food_post where id = " + str(id) 
    c = cursor.execute(query)
    count = c.fetchall()
    left_count = int(count[0][5]) - int(amount)
    print(left_count)
    if left_count<0:
        left_count=left_count + amount
        connection.commit()
        return "405 數量不足"
    else:
        update = "update food_post SET left = "+str(left_count)+" where id = "+str(id) + ";"
        c = cursor.execute(update)
        connection.commit()
        return "200 reserver success"
   
if __name__=="__main__":
    app.run(debug=True)