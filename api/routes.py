from flask import Blueprint, request, jsonify
from .get_table import get_table
from .last_table_update import get_last_table_update

api = Blueprint('api', __name__)

@api.route('/api/v1/lastTableUpdate', methods=['POST'])
def last_table_update():
    input_data = request.json
    response = get_last_table_update(input_data)
    return jsonify(response)

@api.route('/api/v1/getTable', methods=['POST'])
def get_table_endpoint():
    input_data = request.json
    response = get_table(input_data)
    return jsonify(response)
