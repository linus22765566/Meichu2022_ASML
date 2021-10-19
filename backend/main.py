from flask import Flask,request
import sqlite3
app = Flask(__name__)

@app.route('/getAll', methods=['GET'])#跳出所有輪播訊息
def get_all():
    request_data = request.get_json()
    conn =  sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("""select * from food""")
    return  c.fetchall()
    

@app.route('/getDetail/<string:name>', methods=['GET'])#跳出指定圖文訊息 用string name判斷
def get_Detail():
    
    pass

@app.route('/addForm', method=['POST'],)
def add_Form():
    request_data = request.get_json()
    conn =  sqlite3.connect('food.db')
    c = conn.cursor()
    c.execute("""INSERT INTO food VALUES('name','item','location','time','left','max','comment','url')""")
    pass

@app.route('/reserve/<string:name>', method='POST')
def reserve():
    
    pass


if __name__=="__main__":
    app.run(debug=True)
