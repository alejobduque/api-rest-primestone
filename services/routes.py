import json
from flask import Blueprint, jsonify, request
from functions.height import height_to_meters
from functions.primes import get_primes
from models.Models import TableJSON, db

services = Blueprint('services', __name__)


@services.route('/get-prime-numbers/<string:is_prime>')
def get_prime_numbers(is_prime=None):
    try:
        return get_primes(is_prime)
    except Exception as ex:
        return jsonify({'message': 'No fue posible obtener los números primos!'})


@services.route('/convert-height', methods=['POST'])
def convert_height():
    try:
        # Obtiene métrica de altura y la convierte a la unidad de medida metros
        height_inches = float(request.json['height'].split()[0])
        height_meters = height_to_meters(height_inches)

        response_data = request.json
        response_data['height'] = f'{height_meters} metros'
        return jsonify(response_data)
    except Exception as ex:
        return jsonify({'message': 'No fue posible realizar la conversión a metros!'})


@services.route('/set-data', methods=['PUT'])
def set_data():
    try:
        row = TableJSON(name=request.json['name'],
                        height=request.json['height'])
        db.session.add(row)
        db.session.commit()
        return jsonify({"message": "JSON added successfully!"})
    except Exception as ex:
        return jsonify({'message':
                        'No fue agregado el nuevo objeto JSON a la BBDD!'})
