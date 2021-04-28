from flask import Flask, render_template, url_for, flash, redirect
# from .form import RegistrationForm, LoginForm
from form import RegistrationForm, LoginForm
#from app import app
#from app.forms import LoginForm
#from config import config


app = Flask(__name__)

app.config['SECRET_KEY']= '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Ian Kipkoech',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 7, 2021'
    },
    {
        
        'author': 'Odilia Chebet',
        'title': 'Blog post 2',
        'content': 'First post content',
        'date_posted': 'April 8, 2021'
    },
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)    


if __name__=='__main__':
    app.run(debug=True)

 