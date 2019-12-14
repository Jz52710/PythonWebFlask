from flask import Flask,request,render_template,redirect,jsonify,Blueprint

student = Blueprint('student',__name__,url_prefix='/student')

# 链接数据库
import pymysql
db = pymysql.connect(database='students',user='root',password='jz52710',host='127.0.0.1',port=3306)
# 游标
cursor = db.cursor()

# 查
@student.route('/')
def index():
    sql = 'select * from students'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

    return render_template('student.html',data=data)

@student.route('/del')
def dels():
    sql = 'select * from students'
    cursor.execute(sql)
    data = cursor.fetchall()
    for i in data:
        print()
    # print(jsonify({data.data}))
    return jsonify({'code':200,'mag':'ok'})