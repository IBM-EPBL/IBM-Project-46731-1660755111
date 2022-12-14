# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:12:22 2022
@author: Balavignesh.V
"""
from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__   import create_app, db
main = Blueprint('main', __name__)

@main.route('/') 
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
    
@main.route('/about')
def aboutus():
    return render_template('about.html')

app = create_app() 
if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True