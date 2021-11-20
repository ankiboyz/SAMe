# ma.py
""" Herein, the Blueprint implementation of the Moving Averages will go in.
 This structure makes it easy to find related resources and code units pertaining to a functionality.
 This file pertains to the functionality of the Moving Average patterns."""

import config
from flask import Blueprint, request, jsonify
import logging

logger = logging.getLogger(__name__)
ma_bp = Blueprint(name='ma_bp', import_name=__name__
                  , template_folder='templates', static_folder='static'
                  , static_url_path='ma_static')


@ma_bp.route('/')
def list_option():
    """
    This method will list the options those could be passed to the Pattern MA - Moving Average.
    """
    return 'Hi, This is listing of the methods'


@ma_bp.route('/get_pattern', methods=['GET', 'POST']) # supporting both GET and POST.
def get_pattern():
    # Here, let's gather the input parameters.
    # Mainly supporting the POST method.
    if request.method == 'GET':
        return 'Hi, This is the get_pattern method for MA'

    if request.method == 'POST':
        print('request.data', request.data)
        decoded_data = request.data.decode('utf-8')
        print(decoded_data)
