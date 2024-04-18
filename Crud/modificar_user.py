from bson import ObjectId
from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

modify_data_bp = Blueprint('modify_data', __name__)

# Conexión a MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')

# Conectar a la base de datos MongoDB
client = MongoClient(MONGODB_URI)
db = client['prueba1']

# Colección para los usuarios
users_collection = db['login']

@modify_data_bp.route('/get_user/<user_id>')
def get_user(user_id):
    try:
        # Obtener los datos del usuario de la base de datos
        user_data = users_collection.find_one({'_id': ObjectId(user_id)})
        if user_data:
            # Convertir el ObjectId a str para que sea JSON serializable
            user_data['_id'] = str(user_data['_id'])
            return jsonify(user_data)
        else:
            return jsonify({'message': 'El usuario no fue encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al obtener datos del usuario: {str(e)}'}), 500


@modify_data_bp.route('/modify_user_page')
def modify_user_page():
    return render_template('modificar_usuario.html')

@modify_data_bp.route('/modify_user', methods=['POST'])
def modify_user():
    try:
        user_data = request.json
        user_id = user_data.get('user_id')
        if not user_id:
            return jsonify({'message': 'Se requiere el ID del usuario para modificar los datos'}), 400
        
        # Eliminar el ID del usuario de los datos del usuario a modificar
        del user_data['user_id']
        
        # Realizar la actualización en la base de datos
        result = users_collection.update_one({'_id': ObjectId(user_id)}, {'$set': user_data})
        if result.modified_count > 0:
            return jsonify({'message': 'Datos del usuario modificados exitosamente'}), 200
        else:
            return jsonify({'message': 'El usuario con el ID especificado no fue encontrado'}), 404
    except Exception as e:
        return jsonify({'message': f'Error al modificar datos del usuario: {str(e)}'}), 500
