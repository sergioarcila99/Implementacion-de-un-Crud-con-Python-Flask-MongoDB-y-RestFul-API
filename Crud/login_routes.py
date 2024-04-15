from flask import Blueprint, request, session, redirect, url_for,render_template
from pymongo import MongoClient
from bson import ObjectId
import os

login_bp = Blueprint('login', __name__)

# Conexión a MongoDB
MONGODB_URI = os.getenv('MONGODB_URI')

# Conectar a la base de datos MongoDB
client = MongoClient(MONGODB_URI)
db = client['prueba1']

# Colección para los usuarios
users_collection = db['login']

# Ruta para el formulario de inicio de sesión
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener credenciales de inicio de sesión del formulario
        username = request.form['username']
        password = request.form['password']
        
        # Buscar al usuario en la base de datos
        user = users_collection.find_one({'username': username, 'password': password})
        if user:
            # Iniciar sesión del usuario
            session['user_id'] = str(user['_id'])
            return redirect(url_for('login.index'))  # Cambio aquí
        else:
            return 'Credenciales incorrectas. Inténtalo de nuevo.'
    else:
        return '''
            <form method="post">
                <p>Usuario: <input type=text name=username>
                <p>Contraseña: <input type=password name=password>
                <p><input type=submit value=Login>
            </form>
        '''

# Ruta para la página de inicio después de iniciar sesión
@login_bp.route('/')
def index():
    # Verificar si el usuario está autenticado
    if 'user_id' in session:
        # Obtener la información del usuario
        user_id = session['user_id']
        user = users_collection.find_one({'_id': ObjectId(user_id)})
        return render_template('index.html', username=user["username"])
    else:
        return redirect(url_for('login.login'))

# Ruta para cerrar sesión
@login_bp.route('/logout', methods=['POST'])
def logout():
    # Eliminar la sesión del usuario
    session.pop('user_id', None)
    return redirect(url_for('login.login'))

