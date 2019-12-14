from flask import Blueprint,request,render_template,redirect,jsonify
from db.database import Base,engine,session
from db.table import Classroom,serial

import os
classroom = Blueprint('classroom',__name__,url_prefix='/classroom')

# 创建路由

# 传送数据
@classroom.route('/',methods=["GET"])
def cha():
    return render_template('./classroom/classroom.html')
@classroom.route('/addclassroom',methods=["GET"])
def addc():
    return render_template('./classroom/addclassroom.html')

@classroom.route('/get',methods=["GET"])
def getclassroom():
    data = session.query(Classroom).all()
    return jsonify([serial(obj) for obj in data])

#删除
@classroom.route('/del',methods=["delete"])
def deleteclassroom():
    c = session.query(Classroom).filter(Classroom.id).first()
    try:
        session.delete(c)
        session.commit()
    except:
        return jsonify({'code':200,'status':'no','msg':'数据库异常,请稍后重试'})
    return jsonify({'code':200,'status':'yes','msg':"删除成功"})

#添加
@classroom.route('/add',methods=["GET","POST"])
def addclassroom():
    if request.method == "GET":
        return render_template('classroom.html')
    elif request.method == "POST":
        imgs = request.files.get('img')
        file_path = os.path.join('uploads/',imgs.filename)
        imgs.save(file_path)
        msg = Classroom(name=request.form['name'],num=request.form['num'],teacher=request.form['teacher'],img=imgs.filename)

        try:
            session.add(msg)
            session.commit()
        except:
            return jsonify({'code': 200, 'status': 'error', 'msg': '数据库异常'})
        return jsonify({'code':200,'status':'yes','msg':'提交成功'})

# 改
@classroom.route('/edit',methods=["POST"])
def edit():

    session.query(Classroom).filter(Classroom.id==request.form['id'],Classroom.name==request.form['name'], Classroom.num==request.form['num'], Classroom.teacher==request.form['teacher'], Classroom.img==request.form['img']).update({'id':request.form['id'],'name': request.form['name'], 'num': request.form['num'], 'teacher': request.form['teacher'],'img': request.form['img']})
    # print(request.form['num'])
    session.commit()
    return jsonify({'code': 200, 'status': 'yes', 'msg': '提交成功'})