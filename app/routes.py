# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from flask.globals import request
from flask.helpers import flash, url_for
from app import app
from app.models import Region, Material
from app.forms import Choiсe
import re

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # regions_obj = Region.query.all()
    # regions = [x.name for x in regions_obj]

    # materials_obj = Material.query.all()
    # materials = [x.name for x in materials_obj]

    form = Choiсe()

    if form.validate_on_submit():
        region_choices=re.sub("[(|)|']","",form.region.data)
        region_choice = region_choices.split(",")
        material_choices=re.sub("[(|)|']","",form.material.data)
        material_choice = material_choices.split(",")

        flash('Выбран регион: {}. Материал: {}'.format(region_choice[0], material_choice[0]))
        
        flash('Duration: {}'.format(region_choice[1]))
        flash('Temperature: {}'.format(region_choice[2]))

        flash('Thermal: {}'.format(material_choice[1]))
        flash('Depth: {}'.format(material_choice[2]))
        flash('Price: {}'.format(material_choice[3]))

        duration = int(region_choice[1])
        temperature = float(region_choice[2])

        thermal = float(material_choice[1])
        depth = float(material_choice[2])
        price = float(material_choice[3])

        D = (20 - temperature)*duration
        R = 0.00035*D+1.4
        print(R)

        # flash('Расчёт произведён, результаты смотрите ниже.')
        # return redirect(url_for('index'))
    return render_template('index.html', form=form)
    # return render_template('index.html', regions=regions, materials=materials, form=form)
    # return render_template('index.html', form=form)
