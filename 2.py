from flask import Flask,redirect,url_for

app=Flask(__name__)
@app.route('/home')
def index():
	return "<h1>Anjuma nasreen</h1>"
	
@app.route('/index/<name>')
def index1(name):
	#return "<h1>welcome to</h1>" +name
	return "welcome to" +name
	
@app.route('/ind/<age>')
def index2(age):
	return "{}".format(age)
	#return "%d" %age
	
@app.route('/ind/<name>/<age>')
def index3(name,age):
	return "{}	{}".format(name,age)

	
#function mapping
@app.route('/admin')
def admin():
	return "<h1>this is admin page</h1>"
@app.route('/student')
def student():
	return "<h1>this is student page</h1>"
@app.route('/user/<name>')
def home(name):
	if name=='admin':
		return redirect(url_for('admin'))
	if name=='student':
		return redirect(url_for('student'))
	
@app.route('/login')
def login1():
	return render_template('login.html')








if __name__ =='__main__':
	app.run(debug=True)