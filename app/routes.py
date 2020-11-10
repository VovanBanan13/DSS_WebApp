# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    list = ["Республика Мордовия", "Московская область", "Пензенская область","Краснодарский край"]
    return render_template('index.html', option=list)
