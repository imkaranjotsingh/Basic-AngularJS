'''
Created on Jan 10, 2017

@author: hanif
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"


@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/lo/')
def lo():
    return render_template('lo.html')
@app.route('/newtry/')
def newtry():
    return render_template('newtry.html')
@app.route('/hello/')
def hello():
    return render_template('hello.html')
@app.route('/abc/')
def abc():
    return render_template('abc.html')
	
@app.route('/currency/')
def currency():
    return render_template('currency.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = True, port=8181, host="0.0.0.0")
