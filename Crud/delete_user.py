from bson import ObjectId
from flask import Blueprint, jsonify, redirect, render_template, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

delete_data_bp = Blueprint('delete_data', __name__)

# Conexión a MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')

# Conectar a la base de datos MongoDB
client = MongoClient(MONGODB_URI)
db = client['prueba1']

# Colección para los usuarios
users_collection = db['login']

@delete_data_bp.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if request.method == 'DELETE':
        try:
            # Eliminar el usuario de la base de datos MongoDB
            users_collection.delete_one({"_id": ObjectId(user_id)})
            return "Usuario eliminado correctamente", 200
        except:
            return "Error al eliminar el usuario", 500
    else:
        return "Método no permitido", 405
