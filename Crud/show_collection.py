from flask import Blueprint, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

show_collection_bp = Blueprint('show_collection', __name__)

# Conexión a MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')

# Conectar a la base de datos MongoDB
client = MongoClient(MONGODB_URI)
db = client['prueba1']

# Colección para los usuarios
users_collection = db['login']

@show_collection_bp.route('/show_data')
def show_data():
    # Obtener todos los datos de la colección
    data = list(users_collection.find())
    return render_template('collection.html', data=data)
