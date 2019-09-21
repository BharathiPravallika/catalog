from flask import Flask,redirect,url_for,render_template,request
from flask_mail import Mail,Message
from random import randint
from project_database import Register,Base
from sqlalchemy.orm import sessionmaker#(session maker=db to db connection)
from sqlalchemy import create_engine

#engine=create_engine('sqlite:///iiidb')
engine=create_engine('sqlite:///iii.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine#bind=combine to engine
DBsession=sessionmaker(bind=engine)
session=DBsession()


app=Flask(__name__) #defines the project(properties)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='nasreenanjuma471@gmail.com'
app.config['MAIL_PASSWORD']='8501822523'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)
otp=randint(000000,999999)

@app.route("/sample")
def demo():
	return "hello world  hai hiiii welcome"

@app.route("/demo_msg")
def d():
	return "<h1> hello demo page</h1>"

@app.route("/info/details")
def details():
	return "hello details"

@app.route("/details/<name>")
def info(name):
	return "hello {} ".format(name)

@app.route("/details1/<name>/<int:age>/<float:sal>")
def p(name,age,sal):
	return "hello {} age {} and salary {} ".format(name,age,sal)

@app.route("/admin")
def admin():
		return "hello admin"      #moving from 1 fun to another(redirecting

@app.route("/student")
def student():
		return "hello student"

@app.route("/staff")
def sta():
		return "hello staff"

@app.route("/info/<name>")
def admin_info(name):
	if name=='admin':
		return redirect(url_for('admin'))   #function name
	elif name=='student':
		return redirect(url_for("student"))
	elif name=='staff':
		return redirect(url_for("sta"))	
	else:
		return "no url"

#login sample
@app.route("/data")
def demo_html():
	return render_template('login.html')

@app.route("/anju/<name>/<int:age>/<float:sal>")
def arna(name,age,sal):
	return render_template('login.html',n=name,a=age,s=sal)

#table
@app.route("/info-data")
def info_data():
	sno=28
	name='anju'
	branch='cse'
	dept='computerscience'
	return render_template('sample1.html',s=sno,n=name,b=branch,d=dept)

data=[{'sno':786,'name':'anju','branch':'cse','dept':'computerscience'},{'sno':123,'name':'ashu','branch':'cse3','dept':'computerscience3'}]
@app.route("/dummy_data")
def dummy():
	return render_template('samp.html',dummy_data=data)

@app.route("/multiplication_table/<int:number>")
def multiplication_table(number):
	return render_template('mult.html',n=number)

@app.route("/file_upload",methods=['GET','POST'])
def file_upload():
	return render_template("file_upload.html")
@app.route("/success",methods=['GET','POST'])
def success():
	if request.method=='POST':
		f=request.files['file']
		f.save(f.filename)
		return render_template("success.html",f_name=f.filename)





#email and OTP generation
@app.route("/email",methods=['POST','GET'])
def email_send():
	return render_template("email.html")
@app.route("/verify_email",methods=['POST','GET'])
def verify_email():
	email=request.form['email']
	msg=Message("One Time Password",sender="nasreenanjuma471@gmail.com",recipients=[email])
	msg.body=str(otp)
	mail.send(msg)
	return render_template("veri_email.html")

@app.route("/email_success",methods=['POST','GET'])
def success_email():
	user_otp=request.form['otp']
	if otp==int(user_otp):
		return render_template("email_success.html")
	return render_template("verify_email.html")#"invalid otp"

#displaying Table content in browser which was written and added in DB
@app.route("/show")
def showData():
	#register=variable and Register=class name
	register=session.query(Register).all()
	return render_template('show.html',reg=register)

@app.route("/new",methods=['POST','GET'])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],
			surname=request.form['surname'],
			mobile=request.form['mobile'],
			email=request.form['email'],
			branch=request.form['branch'],
			role=request.form['role'])
		session.add(newData)
		#commit is used to save
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('form.html')



















	
if __name__=='__main__':
	app.run(debug=True)               #it should be in the end of the file