# Metodologia de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API

# MONGODB

**Paso a paso para instalar MongoDB en Windows:**

***Descarga MongoDB:*** Ve al sitio web oficial de MongoDB (https://www.mongodb.com/try/download/community) y descarga la versión para Windows.

***Ejecuta el instalador:*** Una vez descargado, ejecuta el archivo de instalación (por lo general, un archivo .msi) y sigue las instrucciones del asistente de instalación.

***Configura la ruta de instalación:*** Durante la instalación, se te pedirá que elijas la carpeta de instalación. Puedes optar por la ruta predeterminada o elegir una personalizada.

***Instala MongoDB Compass (opcional):*** MongoDB Compass es una herramienta gráfica que te permite explorar y administrar tus bases de datos MongoDB. Puedes elegir instalarla durante el proceso de instalación.

***Finaliza la instalación:*** Una vez completada la instalación, asegúrate de que la opción "Agregar a la variable de entorno PATH" esté marcada, esto facilitará el uso de MongoDB desde la línea de comandos.

***Verifica la instalación:*** Abre la línea de comandos (cmd) y escribe mongo --version. Deberías ver la versión de MongoDB que has instalado.

**¿Por qué instalar MongoDB para un proyecto?**

MongoDB es una base de datos flexible y potente que permite una amplia variedad de enfoques para modelar datos y realizar consultas. A continuación, te presento algunas caracteristicas de mongoDB.

***Flexibilidad del esquema***

MongoDB es una base de datos NoSQL, lo que significa que no requiere un esquema fijo como las bases de datos SQL tradicionales. Esto permite una mayor flexibilidad al modelar tus datos, especialmente en proyectos donde los requisitos pueden cambiar con el tiempo.

***Escalabilidad horizontal***

MongoDB está diseñado para la escalabilidad horizontal, lo que significa que puedes distribuir tus datos en múltiples servidores para manejar grandes volúmenes de datos y altas cargas de trabajo.

***Rendimiento***

MongoDB está optimizado para un alto rendimiento, lo que lo hace adecuado para aplicaciones que requieren acceso rápido a grandes cantidades de datos.

***Documentos JSON***

MongoDB almacena los datos en documentos JSON, lo que facilita el mapeo de los datos de tu aplicación a la base de datos, especialmente en entornos donde JavaScript es el lenguaje dominante.

***Comunidad activa y soporte***

MongoDB tiene una gran comunidad de usuarios y una amplia documentación, lo que facilita encontrar ayuda y recursos cuando los necesites.

# FLASK

**Paso a paso para instalar Flask**

***Configuración de Python:*** Si aún no tienes Python instalado en tu sistema, descarga e instala la versión más reciente de Python desde el sitio web oficial (https://www.python.org/downloads/). Durante la instalación, asegúrate de marcar la opción "Agregar Python a PATH".

***Instalación de Flask***

Abre una terminal (cmd) y ejecuta el siguiente comando para instalar Flask utilizando pip, el gestor de paquetes de Python:

*pip install flask*

***Instalacion de los requerimientos***

*pip install Flask-SQLAlchemy*

*pip install pymongo Flask-PyMongo*

*pip install flask_pymongo*

***Crea un proyecto Flask***

Crea una nueva carpeta para tu proyecto Flask y dentro de ella crea un archivo Python (por ejemplo, app.py), que será el punto de entrada de tu aplicación.

***Escribe tu aplicación Flask***

En el archivo app.py, importa Flask y comienza a escribir tu aplicación Flask. Aquí tienes un ejemplo básico para empezar:

*from flask import Flask*

*app = Flask(__name__)*

*@app.route('/')*
*def hello():*
    *return '¡Hola, mundo!'*

*if __name__ == '__main__':*
    ***app.run(debug=True)*

***Ejecuta tu aplicación***

Desde la terminal, navega hasta la carpeta donde guardaste tu archivo app.py y ejecútalo con el siguiente comando:

*python app.py*


**¿Por qué usar Flask para un proyecto?**

***Facilidad de uso:*** Flask es conocido por su simplicidad y facilidad de uso. Es una excelente opción para proyectos pequeños y medianos donde se necesita una solución rápida y ligera.

***Flexibilidad:*** Flask es muy flexible y permite construir aplicaciones web de diversas formas. Puedes agregar extensiones según tus necesidades específicas y no estás limitado por un conjunto rígido de reglas.

***Escalabilidad:*** Aunque Flask es ideal para proyectos más pequeños, también es escalable y puede manejar aplicaciones más grandes con el uso adecuado de extensiones y buenas prácticas de desarrollo.

***Gran comunidad y documentación:*** Flask tiene una gran comunidad de desarrolladores y una amplia documentación disponible en línea. Siempre puedes encontrar ayuda y recursos adicionales para tu proyecto.

En resumen, Flask es una excelente opción para proyectos web que requieren una solución ligera, flexible y fácil de usar.


# PYTHON

**Paso a paso para instalar Python:**

***Descarga de Python:*** Ve al sitio web oficial de Python en https://www.python.org/downloads/ y descarga la última versión de Python para Windows. Puedes elegir entre la versión 3.x, que es la versión más reciente y recomendada para nuevos proyectos.

***Ejecuta el instalador:*** Una vez que se haya descargado el archivo de instalación, ábrelo haciendo doble clic en él. Se abrirá el instalador de Python.

***Configura la instalación:*** En el instalador, asegúrate de marcar la opción "Add Python X.X to PATH" (donde X.X es la versión de Python que estás instalando). Esto agregará Python al PATH de tu sistema, lo que te permitirá ejecutar programas Python desde cualquier ubicación en la línea de comandos.

***Selecciona los componentes:*** Puedes elegir instalar componentes adicionales como pip (el gestor de paquetes de Python) y IDLE (el entorno de desarrollo integrado de Python). Estos son útiles para el desarrollo de proyectos Python, así que te recomendaría que los instales también.

***Completa la instalación:*** Haz clic en "Install Now" para comenzar la instalación. Una vez que la instalación esté completa, haz clic en "Close" para salir del instalador.

***Verifica la instalación:*** Abre una nueva ventana de la línea de comandos (cmd) y escribe python --version. Deberías ver la versión de Python que has instalado. Además, puedes probar escribiendo python y presionando Enter para abrir el intérprete interactivo de Python.


**¿Por qué usar Python para un proyecto?**

***Simplicidad y legibilidad del código***

Python es conocido por su sintaxis simple y legible, lo que lo hace ideal para desarrollar aplicaciones claras y concisas. Esto puede aumentar la productividad y facilitar la colaboración en proyectos de equipo.

***Amplia gama de bibliotecas y frameworks***

Python cuenta con una amplia variedad de bibliotecas y frameworks que cubren casi cualquier necesidad de desarrollo, desde el desarrollo web hasta la inteligencia artificial. Esto hace que Python sea una opción versátil para una amplia gama de proyectos.

***Comunidad activa y soporte***

Python tiene una gran comunidad de desarrolladores en todo el mundo, lo que significa que siempre hay recursos y ayuda disponibles cuando la necesitas. Puedes encontrar tutoriales, documentación y comunidades en línea donde puedes hacer preguntas y obtener respuestas.

***Multiplataforma***

Python es compatible con una amplia gama de plataformas, incluyendo Windows, macOS y Linux. Esto significa que puedes desarrollar tu proyecto en Python y ejecutarlo en diferentes sistemas operativos sin tener que hacer grandes cambios en el código.

En resumen, Python es una excelente opción para una amplia variedad de proyectos debido a su simplicidad, versatilidad y robusta comunidad de desarrolladores.
