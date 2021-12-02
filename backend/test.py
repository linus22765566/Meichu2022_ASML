#databse setup
from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_restful import Api, Resource


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# wrap flask app variable in a new SQLAlchemy object 
db = SQLAlchemy(app)
# ma = Marshmallow(app)
# api = Api(app)



# columnname   data_type       meaning
# id       -> int              primary_key      
# name     -> str              賣家line名稱
# item     -> str              品項名稱
# location -> str              地點
# time     -> DateTime         截止時間
# left     -> int              剩餘數量
# max      -> int              一次最多拿幾份
# comment  -> str              備註
# url      -> str              品項細節頁面
class food_post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(25),nullable=False)
    item = db.Column(db.String(10),nullable=False)
    location = db.Column(db.String(15),nullable=False)
    # time = db.Column(db.DateTime(),nullable=False)
    time = db.Column(db.String(10),nullable=False)
    left = db.Column(db.Integer,nullable=False)
    max = db.Column(db.Integer,nullable=False)
    comment = db.Column(db.String(50),nullable=True)
    url = db.Column(db.String(150),nullable=False)

    def __init__(self, name, item, location, time, left,max,comment,url):
        self.name =name
        self.item = item
        self.location = location
        self.time = time
        self.left = left
        self.max = max
        self.comment = comment
        self.url = url

if __name__== '__main__':
    app.run(debug=True,port=5001)