from flask_app import app
from flask import render_template, redirect, request, session, flash 
from flask_app.models.email import User

@app.route('/')
def create():
    return render_template('email.html')

@app.route('/success', methods= ['POST'])
def success():
    if not User.valid_email(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/results')
    
@app.route('/results')
def validate():
    users = User.get_all()
    return render_template('valid.html', users=users)