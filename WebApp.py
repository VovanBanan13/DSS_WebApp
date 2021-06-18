from app import app, db
from app.models import Region, Material
from app import getApp

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Region': Region, 'Material' : Material}

app = getApp()