# blueprint_registrar.py
"""
This file is the registrar of all the blueprints of the flask defined in this application.
For registration of the blueprint the app object is needed.
"""
from PATTERN.MA.ma import ma_bp


def register_endpoints(app):
    """
    This is the method to register the endpoints
    """
# Registering the views Blueprints
    app.register_blueprint(ma_bp, url_prefix='/SAMe/MA')
