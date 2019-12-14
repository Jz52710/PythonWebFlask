from flask import Flask,render_template,request,redirect,blueprints,jsonify


#导入蓝图
from student import student
# from teach import teach

#实例化web应用
app = Flask(__name__)

app.register_blueprint(student)
# app.register_blueprint(teach)



#创建路由

if __name__ == '__main__':
    app.run(debug=True,port=8000)
