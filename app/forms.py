from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.models import Region, Material

# regions_obj = Region.query.all()
# regions = [x.name for x in regions_obj]

# materials_obj = Material.query.all()
# materials = [x.name for x in materials_obj]

# data = {
#     'region' : regions,
#     'material' : materials
# }

class Choiсe(FlaskForm):
    regions_obj = Region.query.all()
    regions = [x.name for x in regions_obj]

    materials_obj = Material.query.all()
    materials = [x.name for x in materials_obj]

    region = SelectField(u'Выберите регион:',choices=[(r, r) for r in regions])
    material = SelectField(u'Выберите материал:', choices=[(m, m) for m in materials])
    submit = SubmitField('Рассчитать')