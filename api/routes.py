from flask import Blueprint, request, jsonify
from .ws_client import get_last_table_update, get_table

api = Blueprint('api', __name__)

@api.route('/api/v1/lastTableUpdate', methods=['GET'])
def last_table_update():
    physical_name = request.args.get('physicalName')
    if not physical_name:
        return jsonify({"error": "physicalName is required"}), 400

    response = get_last_table_update(physical_name)
    return jsonify(response)

@api.route('/api/v1/getTable', methods=['POST'])
def get_table_endpoint():
    input_data = request.json
    response = get_table(input_data)
    return jsonify(response)
