from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/login')
def login1():
	return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)