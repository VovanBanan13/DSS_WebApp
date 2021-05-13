# -*- coding: utf-8 -*-
from flask import render_template
from app import app
from app.models import Region, Material

@app.route('/')
@app.route('/index')
def index():
    regions_obj = Region.query.all()
    regions = [x.name for x in regions_obj]

    materials_obj = Material.query.all()
    materials = [x.name for x in materials_obj]

    data = {
        'region' : regions,
        'material' : materials
    }

    return render_template('index.html', regions=regions, materials=materials, data=data)
