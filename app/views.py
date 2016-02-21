from flask import render_template,redirect,flash
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


@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login required for :%s and rememberme %s'%(form.openid.data,str(form.remember_me.data)))
		return redirect('/index')

	return render_template('login.html',title='Sign in',form=form,providers=app.config['OPENID_PROVIDERS'])
