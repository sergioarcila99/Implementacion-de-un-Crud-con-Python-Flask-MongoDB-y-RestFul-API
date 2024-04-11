# Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API

CRUD: Es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y Delete (Borrar). Este concepto se utiliza para describir las cuatro operaciones básicas que pueden realizarse en la mayoría de las bases de datos y sistemas de gestión de información.

# Marco Teorico

# API
Las API son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.
# RESTFUL API
Es una API ya implementada que esta construida utilizando la logica de rest, En otras palabras, son el puente de comunicación entre frontend y backend.

**Principios de una API REST (API RESTful)**
Una API RESTful es una interfaz que utiliza los principios de REST para comunicarse hacia y desde un servidor.

El principio más importante en las APIs RESTful es el uso de los métodos HTTP:

GET
POST
PUT
DELETE
Estos métodos son empleados por los clientes para crear, manipular y eliminar datos en los servidores, respectivamente.
# BASE DE DATOS (DB)

# MONGODB
MongoDB es una base de datos NoSQL que se destaca por su flexibilidad y escalabilidad. A diferencia de las bases de datos relacionales, MongoDB no requiere un esquema fijo, lo que significa que puede almacenar datos con estructuras variables en colecciones. En MongoDB, los datos se organizan en bases de datos, colecciones y documentos. Los documentos son objetos JSON que contienen datos y se almacenan en colecciones, similares a las tablas en una base de datos relacional.

Algunas características importantes de MongoDB incluyen su capacidad para escalar horizontalmente, lo que significa que puede distribuir datos entre múltiples servidores para manejar grandes volúmenes de datos y mejorar el rendimiento. MongoDB también ofrece replicación automática de datos para garantizar la alta disponibilidad y la tolerancia a fallos.

MongoDB se utiliza ampliamente en una variedad de aplicaciones, incluyendo aplicaciones web, análisis de datos, gestión de contenido y sistemas IoT. Es especialmente útil cuando se necesitan almacenar y consultar grandes cantidades de datos no estructurados o semi-estructurados de manera eficiente. En resumen, MongoDB es una opción popular para aquellos que buscan una base de datos flexible y escalable para sus aplicaciones.

# MONGODB ATLAS

**MongoDB Atlas** es un servicio de base de datos en la nube completamente gestionado que ofrece todas las capacidades de MongoDB sin la necesidad de configurar ni administrar servidores de base de datos. Permite a los desarrolladores centrarse en la construcción de aplicaciones sin preocuparse por la infraestructura subyacente.

### Características clave:

- **Gestión automática:** Atlas se encarga de la configuración, el escalado y el mantenimiento de los clústeres de MongoDB, liberando a los desarrolladores de tareas de administración.

- **Escalabilidad sencilla:** Permite escalar horizontalmente los clústeres de MongoDB con facilidad, adaptándose a las necesidades cambiantes de las aplicaciones.

- **Alta disponibilidad:** Los clústeres de MongoDB en Atlas se despliegan en múltiples regiones y zonas de disponibilidad para garantizar la alta disponibilidad y la resistencia a fallos.

- **Seguridad avanzada:** Ofrece características de seguridad robustas, como cifrado de datos y autenticación basada en roles, para proteger la integridad de los datos.

- **Integración flexible:** Se integra fácilmente con otras plataformas en la nube y herramientas de desarrollo, simplificando el desarrollo de aplicaciones modernas y escalables.

**MongoDB Atlas** es ampliamente utilizado por empresas de todos los tamaños en una variedad de aplicaciones, desde comercio electrónico hasta análisis de datos, debido a su simplicidad, escalabilidad y seguridad. Es una opción popular para aquellos que buscan una base de datos en la nube fácil de usar y altamente confiable.

# LENGUAJE DE PROGRAMACION

# PYTHON
En el ámbito técnico, Python se define como un lenguaje de programación de alto nivel, con orientación a objetos y una semántica dinámica incorporada, principalmente utilizado para el desarrollo de aplicaciones web y de software. Destaca en el Desarrollo Rápido de Aplicaciones (RAD) debido a su tipificación y encuadernación dinámicas, lo que lo hace atractivo para desarrolladores.

La simplicidad relativa de Python lo convierte en una opción fácil de aprender, gracias a su sintaxis legible y única. Esto facilita la lectura y traducción del código, reduciendo así los costos de mantenimiento y desarrollo del programa. Esto permite a los equipos trabajar juntos sin dificultades significativas de lenguaje y fomenta la experimentación.

¿Para que se usa?

Python es un lenguaje de programación de propósito general, lo que significa que puede aplicarse a una amplia gama de tareas. Su naturaleza interpretada implica que el código escrito no se compila antes de la ejecución, y por eso se le conoce también como un "lenguaje de scripting", originalmente destinado para proyectos simples. Sin embargo, ha evolucionado significativamente y ahora se emplea en la programación de grandes aplicaciones comerciales en lugar de solo aplicaciones básicas.

¿Como Funciona?

El lenguaje de programación Python utiliza módulos de código intercambiables en lugar de largas listas de instrucciones, como era común en los lenguajes de programación funcional. La implementación estándar de Python, conocida como "cpython", no convierte directamente el código en lenguaje de máquina que el hardware pueda entender. En su lugar, lo convierte en un formato llamado "código de bytes", el cual no es legible por la CPU. Por lo tanto, se requiere un intérprete llamado Máquina Virtual Python (PVM) para ejecutar estos códigos de bytes.

El proceso de ejecución de un programa en Python involucra varias etapas:

El intérprete lee el código Python e verifica su sintaxis. Si encuentra algún error, detiene la traducción y muestra un mensaje de error.
Si el código está bien formateado, el intérprete lo traduce a su equivalente en un lenguaje intermedio llamado "código de bytes".
Este código de bytes se envía a la Máquina Virtual Python, donde se ejecuta. Si se produce un error durante esta ejecución, se detiene con un mensaje de error.
# FRAMEWORK

# FLASK

# EDITOR DE CODIGO FUENTE

# VISUAL STUDIO CODE

