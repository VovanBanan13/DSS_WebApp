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
    # regions = [x.name for x in regions_obj]

    materials_obj = Material.query.all()

    # region = SelectField(u'Выберите регион:',choices=[(r, r) for r in regions])
    region = SelectField(u'Выберите регион:', choices=[((r.name, r.duration, r.temperature), r.name) for r in regions_obj])
    material = SelectField(u'Выберите материал:', choices=[((m.name, m.thermal, m.depth, m.price), m.name) for m in materials_obj])
    submit = SubmitField('Рассчитать')