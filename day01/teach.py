from flask import Blueprint,request,render_template,redirect

teach = Blueprint('teach',__name__,url_prefix='/teach')

#连接数据库
import pymysql
db = pymysql.connect(database='teach',user='root',password='jz52710',host='127.0.0.1',port=3306)
cursor = db.cursor()


#查
@teach.route("/teach")
def index():
    #创建游标
    sql = 'select * from teach'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    return render_template("./teach/teach.html",data=data)
# 增
@teach.route("/addteach",methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template("./teach/addteach.html")
    else:
        result = request.form
        sql = "insert into teach (name,num,sex,job,tall) values ('%s','%s','%s','%s','%s')"%(result['name'],result['num'],result['sex'],result['job'],result['tall'])
        cursor.execute(sql)
        db.commit()
        return redirect('/teach/teach')

#删
@teach.route('/del/<id>',methods=['GET'])
def delteach(id):
    sql = 'delete from teach where id=%s'%id
    cursor.execute(sql)
    db.commit()
    return redirect("/teach/teach")
#改
@teach.route('/edit',methods=['POST'])
def edit():
    sql = "update teach set name='%s',num='%s',sex=%s,job='%s',tall='%s' where id=%s" %(request.form['name'],request.form['num'],request.form['sex'],request.form['job'],request.form['tall'],request.form['id'])
    cursor.execute(sql)
    db.commit()
    return "ok"

