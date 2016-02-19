from flask import Flask ,render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return render_template('home.html')
@app.route('/test/<username>')
def hello_world(username):
	return 'hello FLASK world :%s '% username
@app.route('/about/')
def about_us():
	return "Author : Praveenkumar Saminatha"

if __name__=='__main__':
	app.run()
