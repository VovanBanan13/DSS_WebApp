# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from flask.helpers import flash, url_for
from app import app
from app.models import Region, Material
from app.forms import Choiсe

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    regions_obj = Region.query.all()
    regions = [x.name for x in regions_obj]

    materials_obj = Material.query.all()
    materials = [x.name for x in materials_obj]

    form = Choiсe()
    if form.validate_on_submit():
        flash('Расчёт произведён, результаты смотрите ниже. Выбран регион: {}, материалы: {}'.format(form.region.data, form.material.data))
        # flash('Расчёт произведён, результаты смотрите ниже.')
        # return redirect('/')
        return redirect(url_for('index'))
    return render_template('index.html', regions=regions, materials=materials, form=form)
    # return render_template('index.html', form=form)
