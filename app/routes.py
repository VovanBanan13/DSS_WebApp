# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, jsonify
from flask.globals import request
from flask.helpers import flash, url_for
from app import app
from app.models import Region, Material
from app.forms import Choiсe, Choiсe_2, Choiсe_3
import re

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    regions = [{"id": r.id, "name": r.name} for r in Region.query.all()]
    materials = [{"id": m.id, "name": m.name} for m in Material.query.all()]

    data = {
        "regions": regions,
        "materials": materials
    }

    return render_template('index.html', data=data)

@app.route('/calculation', methods=['POST'])
def calculation():
    req_data = request.form
    material_count = len(req_data) - 1
    data = None
    if material_count == 1:
        data = calc1(req_data['region_id'], req_data['materials[0][material_id]'])
    elif material_count == 2:
        data = calc2(req_data['region_id'], req_data['materials[0][material_id]'], req_data['materials[1][material_id]'])
    elif material_count == 3:
        data = calc3(req_data['region_id'], req_data['materials[0][material_id]'], req_data['materials[1][material_id]'], req_data['materials[2][material_id]'])
    return jsonify(data)

def calc1(region_id, material_id):
    region_info = Region.query.get(region_id)
    material_info = Material.query.get(material_id)

    duration = int(region_info.duration)
    temperature = float(region_info.temperature)

    thermal = float(material_info.thermal)
    depth = float(material_info.depth)

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    # S_2 = R * thermal * 1000

    i = 1
    res = 0
    while (res < R):
        res = (depth*i)/(thermal*1000)
        i = i + 1
    S = depth * i

    data = {
        "region": region_info.name,
        "material": material_info.name,
        "results": [{
            "i": i,
            "s": S
        }]
    }

    return data

def calc2(region_id, material_id_1, material_id_2):
    region_info = Region.query.get(region_id)
    duration = int(region_info.duration)
    temperature = float(region_info.temperature)

    material_info_1 = Material.query.get(material_id_1)
    thermal_1 = float(material_info_1.thermal)
    depth_1 = float(material_info_1.depth)

    material_info_2 = Material.query.get(material_id_2)
    thermal_2 = float(material_info_2.thermal)
    depth_2 = float(material_info_2.depth)

    data = {
        "region": region_info.name,
        "material_1": material_info_1.name,
        "material_2": material_info_2.name,
        "results": []
    }

    # data = {
    #     "region": region_info.name,
    #     "materials": [],
    #     "results": []
    # }
    
    # req_data = request.form
    # material_count = len(req_data) - 1
    # for i in material_count:
    #     data['materials'].append({"material" : material_info[i]})

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    for i in range(1, 101):
        S_1 = depth_1 * i
        R_2 = R - ((depth_1 * i)/(thermal_1*1000))
        j = 1
        res = 0
        while (res < R_2):
            res = (depth_2*j)/(thermal_2*1000)
            j = j + 1
        S_2 = depth_2 * j

        data['results'].append({
            "i": i,
            "j":j,
            "s1": S_1,
            "s2": S_2
        })

        if (j == 1):
            break

    return data

def calc3(region_id, material_id_1, material_id_2, material_id_3):
    region_info = Region.query.get(region_id)
    duration = int(region_info.duration)
    temperature = float(region_info.temperature)

    material_info_1 = Material.query.get(material_id_1)
    thermal_1 = float(material_info_1.thermal)
    depth_1 = float(material_info_1.depth)

    material_info_2 = Material.query.get(material_id_2)
    thermal_2 = float(material_info_2.thermal)
    depth_2 = float(material_info_2.depth)

    material_info_3 = Material.query.get(material_id_3)
    thermal_3 = float(material_info_3.thermal)
    depth_3 = float(material_info_3.depth)

    data = {
        "region": region_info.name,
        "material_1": material_info_1.name,
        "material_2": material_info_2.name,
        "material_3": material_info_3.name,
        "results": []
    }

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    for i in range(1, 101):
        R_2 = R - ((depth_1 * i)/(thermal_1*1000))
        S_1 = depth_1 * i
        for j in range(1, 101):
            S_2 = depth_2 * j
            R_3 = R_2 - ((depth_2 * j)/(thermal_2*1000))
            k = 1
            res = 0
            while (res < R_3):
                res = (depth_3*k)/(thermal_3*1000)
                k = k + 1
            S_3 = depth_3 * k
            
            data['results'].append({
            "i": i,
            "j":j,
            "k":k,
            "s1": S_1,
            "s2": S_2,
            "s3": S_3
            })

            if (k == 1):
                break
        if (j == 1):
            break
        
    return data

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
        flash('-----------------------------------')

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
        R = float('{:.4f}'.format(R))

        # R_for = R - ((depth_2 * 1)/(thermal_2*1000))
        # count = int((R_for * thermal_1*1000)/depth_1) + 1
        # flash('Максимальное число: {}'.format(count))
        for i in range(1, 101):
            S_1 = depth_1 * i
            R_2 = R - ((depth_1 * i)/(thermal_1*1000))
            j = 1
            res = 0
            while (res < R_2):
                res = (depth_2*j)/(thermal_2*1000)
                j = j + 1
            S_2 = depth_2 * j
            flash('Толщина {} и {} слоёв составляет: {} мм и {} мм (сумма: {})'.format(i, j, int(S_1), int(S_2), S_1+S_2))
            if (j == 1):
                break             

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
        flash('-----------------------------------')

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
        R = float('{:.4f}'.format(R))

        for i in range(1, 101):
            R_2 = R - ((depth_1 * i)/(thermal_1*1000))
            S_1 = depth_1 * i
            for j in range(1, 101):
                S_2 = depth_2 * j
                R_3 = R_2 - ((depth_2 * j)/(thermal_2*1000))
                k = 1
                res = 0
                while (res < R_3):
                    res = (depth_3*k)/(thermal_3*1000)
                    k = k + 1
                S_3 = depth_3 * k
                flash('Толщина ({}, {}, {}) слоёв составляет: {} мм, {} мм и {} мм (сумма: {})'.format(i, j, k, int(S_1), int(S_2), int(S_3), S_1+S_2+S_3)) 
                if (k == 1):
                    break
            if (j == 1):
                break

    return render_template('3.html', form=form)