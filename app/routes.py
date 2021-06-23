# -*- coding: utf-8 -*-
from flask import render_template, jsonify
from flask.globals import request
from app import app
from app.models import Region, Material

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
    price = float(material_info.price)

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    # S_s = R * thermal * 1000

    i = 1
    res = 0
    while (res < R):
        res = (depth*i)/(thermal*1000)
        i = i + 1
    S = depth * i
    P = price * i

    data = {
        "region": region_info.name,
        "materials": [material_info.name],
        "results": [
            [[i, S, P]]
        ]
    }

    return data

def calc2(region_id, material_id_1, material_id_2):
    region_info = Region.query.get(region_id)
    duration = int(region_info.duration)
    temperature = float(region_info.temperature)

    material_info_1 = Material.query.get(material_id_1)
    thermal_1 = float(material_info_1.thermal)
    depth_1 = float(material_info_1.depth)
    price_1 = float(material_info_1.price)

    material_info_2 = Material.query.get(material_id_2)
    thermal_2 = float(material_info_2.thermal)
    depth_2 = float(material_info_2.depth)
    price_2 = float(material_info_2.price)

    data = {
        "region": region_info.name,
        "materials": [material_info_1.name, material_info_2.name],
        "results": []
    }

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    for i in range(1, 101):
        S_1 = depth_1 * i
        P_1 = price_1 * i
        R_2 = R - ((depth_1 * i)/(thermal_1*1000))
        j = 1
        res = 0
        while (res < R_2):
            res = (depth_2*j)/(thermal_2*1000)
            j = j + 1
        S_2 = depth_2 * j
        P_2 = price_2 * j

        data['results'].append(
            [[i, S_1, P_1], [j, S_2, P_2]]
        )

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
    price_1 = float(material_info_1.price)

    material_info_2 = Material.query.get(material_id_2)
    thermal_2 = float(material_info_2.thermal)
    depth_2 = float(material_info_2.depth)
    price_2 = float(material_info_2.price)

    material_info_3 = Material.query.get(material_id_3)
    thermal_3 = float(material_info_3.thermal)
    depth_3 = float(material_info_3.depth)
    price_3 = float(material_info_3.price)

    data = {
        "region": region_info.name,
        "materials": [material_info_1.name, material_info_2.name, material_info_3.name],
        "results": []
    }

    D = (20 - temperature)*duration
    R = 0.00035*D+1.4
    R = float('{:.4f}'.format(R))

    for i in range(1, 101):
        R_2 = R - ((depth_1 * i)/(thermal_1*1000))
        S_1 = depth_1 * i
        P_1 = price_1 * i
        for j in range(1, 101):
            S_2 = depth_2 * j
            P_2 = price_2 * j
            R_3 = R_2 - ((depth_2 * j)/(thermal_2*1000))
            k = 1
            res = 0
            while (res < R_3):
                res = (depth_3*k)/(thermal_3*1000)
                k = k + 1
            S_3 = depth_3 * k
            P_3 = price_3 * k
            
            data['results'].append(
                [[i, S_1, P_1], [j, S_2, P_2], [k, S_3, P_3]]
            )

            if (k == 1):
                break
        if (j == 1):
            break
        
    return data
