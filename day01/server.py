from flask import Flask,render_template,request,redirect,blueprints,jsonify,abort
from db.database import Base,engine,session

#导入蓝图
from student import student
from teach import teach
from classroom import classroom
# from outside import outside

#实例化web应用
app = Flask(__name__)

app.register_blueprint(student)
app.register_blueprint(teach)
app.register_blueprint(classroom)

# app.register_blueprint(outside)

# @app.route('/')
# def index():
#     data = session.query(Student).all()
#     return jsonify([serial(obj) for obj in data])
#     #abort 快速返回 错误相应

#创建路由

if __name__ == '__main__':
    app.run(debug=True,port=8000)
    Base.metadate.create_all(engine)
