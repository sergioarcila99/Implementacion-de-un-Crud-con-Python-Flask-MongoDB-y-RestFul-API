from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import os
from flask import jsonify


main_bp = Blueprint('main', __name__)

@main_bp.route('/get_data', methods=['GET'])
def get_data():
    # Obtener parámetros de la solicitud
    db_name = request.args.get('db_name')
    collection_name = request.args.get('collection_name')
    
    # Conexión a MongoDB
    MONGODB_URI = os.getenv('MONGODB_URI')
    client = MongoClient(MONGODB_URI)
    
    # Acceder a la base de datos y la colección seleccionadas
    db = client[db_name]
    collection = db[collection_name]
    
    # Obtener todos los documentos de la colección seleccionada
    data = list(collection.find())
    
    # Devolver los datos como respuesta
    return jsonify({'data': data})
