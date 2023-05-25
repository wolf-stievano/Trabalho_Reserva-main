from flask import Blueprint, request, jsonify
from bson.objectid import ObjectId
from settings import reservations_collection

reservations_blueprint = Blueprint('reservations', __name__)

# Criar uma tarefa (C)
@reservations_blueprint.route('/reservations', methods=['POST'])
def create_reservation():
    reservation = request.get_json()
    result = reservations_collection.insert_one(reservation)
    reservation['_id'] = str(result.inserted_id)
    return jsonify(reservation), 201

# Obter todas as tarefas (R)
@reservations_blueprint.route('/reservations/<user_id>', methods=['GET'])
def get_reservations(user_id):
    reservations = []
    for reservation in reservations_collection.find({"user_id": user_id}):  # filtrando as tarefas baseado no usuário autenticado
        reservation['_id'] = str(reservation['_id'])
        reservations.append(reservation)
    return jsonify(reservations), 200


# Atualizar uma tarefa (U)
@reservations_blueprint.route('/reservations/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    updated_reservation = request.get_json()
    updated_reservation.pop('_id', None) 
    reservations_collection.update_one({'_id': ObjectId(reservation_id)}, {'$set': updated_reservation})
    return jsonify(updated_reservation), 200

# Deletar uma tarefa (D)
@reservations_blueprint.route('/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservations_collection.delete_one({'_id': ObjectId(reservation_id)})
    return jsonify({'result': 'reservation deleted'}), 200
