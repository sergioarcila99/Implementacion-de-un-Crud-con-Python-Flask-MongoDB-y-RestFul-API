from flask import Flask, redirect, url_for
from login_routes import login_bp
from show_collection import show_collection_bp
from create_user import create_user_bp
from modificar_user import modify_data_bp
import os 
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para la sesión

# Registrar el Blueprint del login en la aplicación
app.register_blueprint(login_bp)

# Registrar el Blueprint de la colección en la aplicación
app.register_blueprint(show_collection_bp)

# Registrar el Blueprint de la creacion de usuarios en la aplicación 
app.register_blueprint(create_user_bp)

# Registrar el Blueprint de la modificacion de usuarios en la aplicación 
app.register_blueprint(modify_data_bp)


# Ruta para redirigir al login
@app.route('/')
def redirect_to_login():
    return redirect(url_for('login.login'))

# Resto del código permanece igual...

if __name__ == '__main__':
    app.run(debug=True)
