from flask import Blueprint,request,render_template

outside = Blueprint('outside',__name__,url_prefix='/')

@outside.route("/")
def index():
    return render_template("./outside.html")

# @teach.route("/addteach",methods=['GET','POST'])
# def add():
#     if request.method == 'GET':
#         return render_template("./teach/addteach.html")
#     else:
#         print(request.form)
#         print(request.form['name'],request.form['sex'],request.form['age'],request.form['idcard'],request.form['class'])
#         result = request.form
#         return render_template('./teach/teach.html',result = result)