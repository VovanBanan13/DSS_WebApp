# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from flask.globals import request
from flask.helpers import flash, url_for
from app import app
from app.models import Region, Material
from app.forms import Choiсe, Choiсe_2, Choiсe_3
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
        flash('-----------------------------------')
        flash('Duration: {}'.format(region_choice[1]))
        flash('Temperature: {}'.format(region_choice[2]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice[1]))
        flash('Depth: {}'.format(material_choice[2]))
        flash('Price: {}'.format(material_choice[3]))
        flash('-----------------------------------')

        duration = int(region_choice[1])
        temperature = float(region_choice[2])

        thermal = float(material_choice[1])
        depth = float(material_choice[2])
        price = float(material_choice[3])

        D = (20 - temperature)*duration
        R = 0.00035*D+1.4
        R = float('{:.3f}'.format(R))
        print(R)

        S = R * thermal * 1000
        flash('Толщина слоя из "{}" по формуле составляет {} мм'.format(material_choice[0], int(S)))

        i = 1
        res = 0
        while (res < R):
            res = (depth*i)/(thermal*1000)
            i = i + 1
            # print('#{}: {}'.format(i, res))
        S_2 = depth * i
        flash('Толщина {} слоёв составляет: {} мм'.format(i, int(S_2)))

        # flash('Расчёт произведён, результаты смотрите ниже.')
        # return redirect(url_for('index'))
    return render_template('index.html', form=form)
    # return render_template('index.html', regions=regions, materials=materials, form=form)
    # return render_template('index.html', form=form)

@app.route('/2', methods=['GET', 'POST'])
def lay_2():
    
    form = Choiсe_2()

    if form.validate_on_submit():
        region_choices=re.sub("[(|)|']","",form.region.data)
        region_choice = region_choices.split(",")
        material_choices_1=re.sub("[(|)|']","",form.material_1.data)
        material_choice_1 = material_choices_1.split(",")
        material_choices_2=re.sub("[(|)|']","",form.material_2.data)
        material_choice_2 = material_choices_2.split(",")

        flash('Выбран регион: {}. Материалы: {} и {}'.format(region_choice[0], material_choice_1[0], material_choice_2[0]))
        flash('-----------------------------------')
        flash('Duration: {}'.format(region_choice[1]))
        flash('Temperature: {}'.format(region_choice[2]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice_1[1]))
        flash('Depth: {}'.format(material_choice_1[2]))
        flash('Price: {}'.format(material_choice_1[3]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice_2[1]))
        flash('Depth: {}'.format(material_choice_2[2]))
        flash('Price: {}'.format(material_choice_2[3]))

        duration = int(region_choice[1])
        temperature = float(region_choice[2])

        thermal_1 = float(material_choice_1[1])
        depth_1 = float(material_choice_1[2])
        price_1 = float(material_choice_1[3])

        thermal_2 = float(material_choice_2[1])
        depth_2 = float(material_choice_2[2])
        price_2 = float(material_choice_2[3])

        D = (20 - temperature)*duration
        R = 0.00035*D+1.4

    return render_template('2.html', form=form)

@app.route('/3', methods=['GET', 'POST'])
def lay_3():
    
    form = Choiсe_3()

    if form.validate_on_submit():
        region_choices=re.sub("[(|)|']","",form.region.data)
        region_choice = region_choices.split(",")
        material_choices_1=re.sub("[(|)|']","",form.material_1.data)
        material_choice_1 = material_choices_1.split(",")
        material_choices_2=re.sub("[(|)|']","",form.material_2.data)
        material_choice_2 = material_choices_2.split(",")
        material_choices_3=re.sub("[(|)|']","",form.material_3.data)
        material_choice_3 = material_choices_3.split(",")

        flash('Выбран регион: {}. Материалы: {} и {} и {}'.format(region_choice[0], material_choice_1[0], material_choice_2[0], material_choice_3[0]))
        flash('-----------------------------------')
        flash('Duration: {}'.format(region_choice[1]))
        flash('Temperature: {}'.format(region_choice[2]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice_1[1]))
        flash('Depth: {}'.format(material_choice_1[2]))
        flash('Price: {}'.format(material_choice_1[3]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice_2[1]))
        flash('Depth: {}'.format(material_choice_2[2]))
        flash('Price: {}'.format(material_choice_2[3]))
        flash('-----------------------------------')
        flash('Thermal: {}'.format(material_choice_3[1]))
        flash('Depth: {}'.format(material_choice_3[2]))
        flash('Price: {}'.format(material_choice_3[3]))

        duration = int(region_choice[1])
        temperature = float(region_choice[2])

        thermal_1 = float(material_choice_1[1])
        depth_1 = float(material_choice_1[2])
        price_1 = float(material_choice_1[3])

        thermal_2 = float(material_choice_2[1])
        depth_2 = float(material_choice_2[2])
        price_2 = float(material_choice_2[3])

        thermal_3 = float(material_choice_3[1])
        depth_3 = float(material_choice_3[2])
        price_3 = float(material_choice_3[3])

        D = (20 - temperature)*duration
        R = 0.00035*D+1.4

    return render_template('3.html', form=form)