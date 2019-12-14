from flask import Blueprint,request,render_template,redirect,jsonify
#蓝图
#1.导入蓝图
#2.注册蓝图
student = Blueprint('student',__name__,url_prefix="/student")

#连接数据库
import pymysql
db = pymysql.connect(database='students',user='root',password='jz52710',host='127.0.0.1',port=3306)
cursor = db.cursor()

# 查
@student.route("/student")
def index():
    # 创建游标
    sql = 'select * from students'
    cursor.execute(sql)
    data = cursor.fetchall()
    # print(data)

    return render_template("student.html",data=data)

# 增
@student.route("/add",methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template("add.html")
    else:
        print(request.form)
        print(request.form['name'],request.form['sex'],request.form['age'],request.form['idcard'],request.form['class'])
        result = request.form
        sql = "insert into students (num,name,age,sex,class) values ('%s','%s','%s','%s','%s')"%(result['idcard'],result['name'],result['age'],result['sex'],result['class'])
        cursor.execute(sql)
        db.commit()
        return redirect('/student/student')

# 删除
@student.route('/del/<id>',methods=['GET'])
def delstu(id):
    sql = 'delete from students where id=%s'%id
    cursor.execute(sql)
    # 更新数据库
    db.commit()

    return redirect("/student/student")
# 改
@student.route('/edit',methods=['POST'])
def edit():
    sql = "update students set num ='%s',name='%s',age=%s,sex=%s,class='%s' where id=%s"%(request.form['idcard'],request.form['name'],request.form['age'],request.form['sex'],request.form['class'],request.form['id'])
    cursor.execute(sql)
    db.commit()
    return "ok"