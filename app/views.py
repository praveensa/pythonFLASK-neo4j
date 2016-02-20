from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user= { 'nickname' : 'Praveenkumar'}
	posts=[
		{'author':{'nickname':'Hari'},
		'content':'Nammooru Bengaloruuu'},
		{'author':{'nickname':'Ara'},
                'content':'Namma ooru madrasu ithuku naakathanae addressu'},
		{'author':{'nickname':'Maha'},
                'content':'Bavi ooru namma ooru'
		}
		]


	return render_template('index.html',user=user,title='Home',posts=posts)


@app.route('/login')
def login():
	form=LoginForm()
	return render_template('login.html',form=form,title='sign_in')
