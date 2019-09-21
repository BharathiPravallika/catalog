from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

def staff():
	return "hello staff"
@app.route("/info/<name>")
def admin_info(name):
	if name=='admin':
		retun redirect(url_for('staff'))
	else
		return "no url"
	@app route("/data/<name>/<int:age>/<float:sal>")
	def demo_html(name,age,sal):
		return render_template('login.html',n=name,a=age,s=sal)


if __name__ =='__main__':
	app.run(debug=True)