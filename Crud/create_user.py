from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

create_user_bp = Blueprint('create_user', __name__)

# Conexión a MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')

# Conectar a la base de datos MongoDB
client = MongoClient(MONGODB_URI)
db = client['prueba1']

# Colección para los usuarios
users_collection = db['login']

@create_user_bp.route('/create_user', methods=['POST'])
def create_user():
    # Obtener los datos del usuario del cuerpo de la solicitud
    user_data = request.json
    
    # Verificar si los datos requeridos están presentes
    if 'nombre' not in user_data or 'edad' not in user_data or 'username' not in user_data or 'password' not in user_data:
        return jsonify({'message': 'Se requiere nombre, edad y un usuario con contraseña para crear un usuario'}), 400
    
    # Insertar el documento del usuario en la colección
    try:
        result = users_collection.insert_one(user_data)
        return jsonify({'message': 'Usuario creado exitosamente', 'inserted_id': str(result.inserted_id)}), 201
    except Exception as e:
        return jsonify({'message': f'Error al crear usuario: {str(e)}'}), 500

@create_user_bp.route('/create_user_page')
def create_user_page():
    return render_template('crear_usuario.html')