# SAMe_app.py
"""
Here, this file creates the SAMe app.
And also calls the blueprint_registrar to register the endpoints to this app.
"""
from flask import Flask
import blueprint_registrar


def create_app():
    """
    This method is to create the app.
    Call the registration endpoints method.
    """

    app = Flask(__name__)

    # Register the endpoints.
    blueprint_registrar.register_endpoints(app)

    return app