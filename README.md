# Implementacion-de-un-Crud-con-Python-Flask-MongoDB-Replica Set-y-RestFul-API

CRUD: Es el acrónimo de Create (Crear), Read (Leer), Update (Actualizar) y Delete (Borrar). Este concepto se utiliza para describir las cuatro operaciones básicas que pueden realizarse en la mayoría de las bases de datos y sistemas de gestión de información.

**Integrantes**
- Jhon Jairo Rendon Zavala
- Sergio Luis Arcila Quiceno

# Marco Teorico

# REST

La transferencia de estado representacional (REST) es una arquitectura de software que impone condiciones sobre cómo debe funcionar una API. En un principio, REST se creó como una guía para administrar la comunicación en una red compleja como Internet. Es posible utilizar una arquitectura basada en REST para admitir comunicaciones confiables y de alto rendimiento a escala. Puede implementarla y modificarla fácilmente, lo que brinda visibilidad y portabilidad entre plataformas a cualquier sistema de API.

**Por qué debemos utilizar REST**

- Crea una petición HTTP que contiene toda la información necesaria, es decir, un REQUEST a un servidor tiene toda la información necesaria y solo espera una RESPONSE, ósea una respuesta en concreto.
- Se apoya sobre un protocolo que es el que se utiliza para las páginas web, que es HTTP, es un protocolo que existe hace muchos años y que ya está consolidado, no se tiene que inventar ni realizar cosas nuevas.
- Se apoya en los métodos básicos de HTTP, como son:
  **Post:** Para crear recursos nuevos.
  **Get:** Para obtener un listado o un recurso en concreto.
  **Put:** Para modificar.
  **Patch:** Para modificar un recurso que no es un recurso de un dato, por ejemplo.
  **Delete:** Para borrar un recurso, un dato por ejemplo de nuestra base de datos.

# API
Las API son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.

![API-Application-Programming-Interfaces](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/9b99e6cd-9203-43d4-8fc5-6125cd6c6c54)

*Tomado de:* https://es.abstracta.us/blog/api-testing-guia-practica/


# RESTFUL API

Las API RESTful es practicamente una parte fundamental del proyecto ya que su arquitectura basada en estándares nos proporciona un enfoque claro y consistente para diseñar nuestras API, lo que facilita su comprensión y mantenimiento. Además, su naturaleza basada en HTTP nos permite aprovechar todo el potencial de la web, incluyendo la caché, la seguridad y la escalabilidad inherentes al protocolo HTTP. La modularidad y la escalabilidad de las API RESTful nos permiten construir servicios web flexibles y extensibles que pueden adaptarse fácilmente a los cambios en los requisitos del proyecto.

Es una API ya implementada que esta construida utilizando la logica de rest, En otras palabras, son el puente de comunicación entre frontend y backend.

![rest-api](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/843f1035-d17d-4d62-95b2-7e8034566b6c)

*Tomado de:* https://mannhowie.com/rest-api

**Principios de una API REST (API RESTful)**

Una API RESTful es una interfaz que utiliza los principios de REST para comunicarse hacia y desde un servidor.

El principio más importante en las APIs RESTful es el uso de los métodos HTTP: GET, POST, PUT, DELETE. 
Estos métodos son empleados por los clientes para crear, manipular y eliminar datos en los servidores, respectivamente.
# BASE DE DATOS (DB)

# MONGODB

MongoDB es importante en nuestro proyecto por varias razones clave. En primer lugar, su modelo de datos flexible nos permite manejar una variedad de tipos de datos de manera eficiente, lo que es fundamental dado el alcance variable de la implementacion. Además, su capacidad para escalar horizontalmente nos brinda la flexibilidad necesaria para adaptarnos a cambios en la demanda y en el volumen de datos a medida que nuestro proyecto crece. Esto asegura que podamos mantener un rendimiento óptimo sin comprometer la disponibilidad. Además, la capacidad de MongoDB para trabajar con grandes conjuntos de datos y realizar consultas complejas de manera eficiente nos permite obtener información valiosa de nuestros datos, lo que es crucial para la toma de decisiones informadas en nuestro proyecto.

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


**REPLICA SET**

Un conjunto de réplicas es un grupo de mongodb en instancias que mantienen el mismo conjunto de datos. Un conjunto de réplicas contiene varios nodos que contienen datos y, opcionalmente, un nodo árbitro. De los nodos que contienen datos, uno y sólo un miembro se considera nodo primario, mientras que los demás nodos se consideran nodos secundarios.

El nodo principal recibe todas las operaciones de escritura. Un conjunto de réplicas puede tener solo un primario capaz de confirmar escrituras con problemas de escritura; aunque en algunas circunstancias, otra instancia de mongodb puede creer transitoriamente que también es primaria. El primario registra todos los cambios en sus conjuntos de datos en su registro de operaciones, es decir, oplog . 

Los secundarios replican el registro de operaciones del primario y aplican las operaciones a sus conjuntos de datos de manera que los conjuntos de datos de los secundarios reflejen el conjunto de datos del primario. Si la primaria no está disponible, una secundaria elegible llevará a cabo una elección para elegirse a sí misma como la nueva primaria.

En algunas circunstancias (por ejemplo, si tiene una instancia primaria y una secundaria pero las restricciones de costos prohíben agregar otra secundaria), puede optar por agregar una mongodb en instancia a un conjunto de réplicas como árbitro . Un árbitro participa en las elecciones pero no retiene datos (es decir, no proporciona redundancia de datos).

![replicaset1](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/205398dd-ec8e-4625-bee1-ab7219e6bdca)

*Tomado de:* https://aesale.towncabco.com/category?name=mongodb%20replica%20set%20tutorial

**Consideraciones al implementar un conjunto de réplicas**

- Arquitectura
- Nombres de host
- Enlace de IP
- Conectividad
- Configuración


# LENGUAJE DE PROGRAMACION

# PYTHON

Python es una elección fundamental para nuestro proyecto por diversas razones. su sintaxis clara y legible facilita el desarrollo y mantenimiento del código, lo que aumenta la productividad del equipo. Además, la amplia gama de bibliotecas y frameworks disponibles en Python nos brinda acceso a herramientas especializadas para diferentes aspectos de nuestro proyecto, desde el análisis de datos hasta el desarrollo web. La versatilidad de Python también nos permite construir prototipos rápidamente y escalar nuestras soluciones según sea necesario a medida que nuestro proyecto evoluciona. se puede decir entonces que, Python ofrece la combinación perfecta de facilidad de uso, potencia y soporte comunitario que necesitamos para tener éxito en nuestro proyecto.

En el ámbito técnico, Python se define como un lenguaje de programación de alto nivel, con orientación a objetos y una semántica dinámica incorporada, principalmente utilizado para el desarrollo de aplicaciones web y de software. Destaca en el Desarrollo Rápido de Aplicaciones (RAD) debido a su tipificación y encuadernación dinámicas, lo que lo hace atractivo para desarrolladores.

La simplicidad relativa de Python lo convierte en una opción fácil de aprender, gracias a su sintaxis legible y única. Esto facilita la lectura y traducción del código, reduciendo así los costos de mantenimiento y desarrollo del programa. Esto permite a los equipos trabajar juntos sin dificultades significativas de lenguaje y fomenta la experimentación.

**¿Para que se usa?**

Python es un lenguaje de programación de propósito general, lo que significa que puede aplicarse a una amplia gama de tareas. Su naturaleza interpretada implica que el código escrito no se compila antes de la ejecución, y por eso se le conoce también como un "lenguaje de scripting", originalmente destinado para proyectos simples. Sin embargo, ha evolucionado significativamente y ahora se emplea en la programación de grandes aplicaciones comerciales en lugar de solo aplicaciones básicas.

**¿Como Funciona?**

El lenguaje de programación Python utiliza módulos de código intercambiables en lugar de largas listas de instrucciones, como era común en los lenguajes de programación funcional. La implementación estándar de Python, conocida como "cpython", no convierte directamente el código en lenguaje de máquina que el hardware pueda entender. En su lugar, lo convierte en un formato llamado "código de bytes", el cual no es legible por la CPU. Por lo tanto, se requiere un intérprete llamado Máquina Virtual Python (PVM) para ejecutar estos códigos de bytes.

![python-articulo](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/ecb5f58e-02b8-4e56-bb7a-1ddf783beea2)

*Tomado de:* https://www.cnac.es/noticias/que-es-python/

El proceso de ejecución de un programa en Python involucra varias etapas:

El intérprete lee el código Python e verifica su sintaxis. Si encuentra algún error, detiene la traducción y muestra un mensaje de error.
Si el código está bien formateado, el intérprete lo traduce a su equivalente en un lenguaje intermedio llamado "código de bytes".
Este código de bytes se envía a la Máquina Virtual Python, donde se ejecuta. Si se produce un error durante esta ejecución, se detiene con un mensaje de error.

# FRAMEWORK
Un framework es una estructura diseñada para simplificar la resolución de problemas comunes en programación. Estas herramientas agilizan el proceso al ayudar con la organización del código y la colaboración en equipos de trabajo. En esencia, los frameworks tienen como propósito hacer más fácil el trabajo de los programadores.

Además, es importante señalar que muchos de estos frameworks no solo facilitan la organización del trabajo, sino que también proporcionan recursos desarrollados por otros programadores. Estos recursos pueden incluir informes o códigos que pueden ser utilizados para abordar problemas comunes en la realización de tareas específicas.

**Tipos de framework**

**Frameworks para software development**
Los frameworks para aplicaciones generales se utilizan para mejorar la estructura de una aplicación. Su objetivo es proporcionar una estructura base para los desarrolladores de software con la que puedan organizar sus proyectos. Eso sí, siempre dentro de un sistema operativo determinado. 

**Frameworks para desarrollo web**
Al estar relacionados con el diseño web, es evidente que existen diferentes frameworks para los diferentes lenguajes de programación que se utilizan. Un desarrollador backend y uno de frontend usarán marcos de trabajo distintos, aunque existen algunos ideales para los full stack developers como ReactJS.

**Marco de gestión de contenido**
De nuevo, un tipo de frameworks relacionados con el diseño web. Aun así, en este caso se trata de interfaces diseñadas para personalizar un CMS. En consecuencia, existen una gran cantidad de CMFs, ideales para diferentes lenguajes e incluso para diferentes tareas dentro de un lenguajes.

# FLASK

Flask es una opción esencial para nuestro proyecto por varias razones cruciales. En primer lugar, su simplicidad y minimalismo nos permiten construir aplicaciones web de manera rápida y eficiente, sin la sobrecarga de características innecesarias. Esto significa que podemos centrarnos en desarrollar funcionalidades específicas de nuestro proyecto sin distracciones. Además, la flexibilidad de Flask nos permite crear aplicaciones web de cualquier tamaño o complejidad, desde pequeñas API hasta aplicaciones web completas. es decir, Flask ofrece la combinación perfecta de simplicidad, flexibilidad y soporte comunitario que necesitamos para construir con éxito nuestro proyecto web.

Flask es un framework escrito en Python que permite crear aplicaciones de forma sencilla y rápida. Es decir, un acelerador de tareas que funciona con pocas líneas de código y que ejecuta las aplicaciones rápidamente. 

![Captura-de-pantalla-615](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/8e8980c2-8b9c-4d4d-af33-8d7714b6eefa)

*Tomado de:* https://keepcoding.io/blog/como-funciona-programa-con-flask-y-servidor-web/

**Ventajas de usar Flask**  
Las ventajas de flask son las mismas ventajas que aporta un framework cualquiera. Aunque hablando de flask, podemos concretarla en las siguientes. 

- **Estructura del proyecto:** las apps que se construyen con Flask tienen elementos y ficheros idénticos. Hay una estructura y se puede seguir al dedillo, facilitando las tareas.
   
- **Colaboración facilitada:** colaboración entre programadores que quieran entrar a inspeccionar el proyecto que estás creando.
  
- **Biblioteca:** Es fácil encontrar bibliotecas adaptadas al Framework.

**Por qué usar Flask**
- **Flask es un “micro” Framework:** Para desarrollar una App básica o que se quiera desarrollar de una forma ágil y rápida Flask puede ser muy conveniente, para determinadas aplicaciones no se necesitan muchas extensiones y es suficiente.
- **Incluye un servidor web de desarrollo:** No se necesita una infraestructura con un servidor web para probar las aplicaciones sino de una manera sencilla se puede correr un servidor web para ir viendo los resultados que se van obteniendo.
- **Tiene un depurador y soporte integrado para pruebas unitarias:** Si tenemos algún error en el código que se está construyendo se puede depurar ese error y se puede ver los valores de las variables. Además está la posibilidad de integrar pruebas unitarias.
- Es compatible con Python3.
- **Es compatible con wsgi:** Wsig es un protocolo que utiliza los servidores web para servir las páginas web escritas en Python.
- **Buen manejo de rutas:** Cuando se trabaja con Apps Web hechas en Python se tiene el controlador que recibe todas las peticiones que hacen los clientes y se tienen que determinar que ruta está accediendo el cliente para ejecutar el código necesario.
- Soporta de manera nativa el uso de cookies seguras.
- Se pueden usar sesiones.
- **Flask no tiene ORMs:** Pero se puede usar una extensión.
- Sirve para construir servicios web (como APIs REST) o aplicaciones de contenido estático.
- Flask es Open Source y está amparado bajo una licencia BSD.
- Buena documentación, código de GitHub y lista de correos.
# EDITOR DE CODIGO FUENTE

Los editores de código son las herramientas que todo desarrollador debe tener a mano. Permiten editar código fuente en diversos lenguajes de programación y ofrecen múltiples herramientas para facilitar el trabajo y aumentar la productividad.

Debemos distinguir entre editores de código e IDE. Los editores generalmente son programas ligeros, que ofrecen lo necesario para poder ser productivos y tener una experiencia de desarrollo adecuada, pero sin compliaciones.

Sin embargo, los editores actuales se pueden extender tanto como se quiera, por medio de complementos que los pueden hacer llegar a ser tan avanzados como los IDE.

**Algunos editores de codigo**

- Visual Studio Code
- Notepad ++
- Brackets
- Komodo Edit
- Phoenix Editor
- CodeLobster
- PSPad

# VISUAL STUDIO CODE

Visual Studio Code es una herramienta imprescindible para nuestro proyecto por varias razones clave. En primer lugar, su interfaz de usuario intuitiva y su diseño ergonómico hacen que sea fácil de usar y aumentan nuestra productividad durante el desarrollo. Además, su amplia gama de extensiones y complementos nos permite personalizar y adaptar el entorno de desarrollo según nuestras necesidades específicas, desde la integración con control de versiones hasta la depuración avanzada y la autocompletación de código. La capacidad de Visual Studio Code para trabajar con una variedad de lenguajes de programación y tecnologías nos permite desarrollar nuestro proyecto de manera efectiva, independientemente de las tecnologías que estemos utilizando. 

Visual Studio Code, también conocido como VSCode, es un editor de código gratuito, de código abierto y compatible con múltiples plataformas, diseñado para programadores. Desarrollado por Microsoft, una empresa con una larga trayectoria en la creación de entornos de desarrollo integrados (IDEs), ha logrado ofrecer una herramienta ligera y práctica que ha sido ampliamente adoptada por la comunidad.

A pesar de que su nombre evoca a otra herramienta de Microsoft, Visual Studio IDE, VSCode es una aplicación independiente desarrollada con una base de código diferente y utilizando tecnologías completamente distintas. A diferencia de Visual Studio, orientado principalmente a los lenguajes y tecnologías exclusivas de Microsoft, VSCode es versátil y puede adaptarse a cualquier lenguaje de programación imaginable.

VSCode nos permite comenzar a editar con una buena cantidad de herramientas de base que nos evita configurar nada en el editor para disponer de una experiencia de desarrollo bastante buena. Actualmente VSCode es el editor más usado para programadores, con una diferencia disparada de sus competidores. Existen extensiones para personalizarlo para cantidad de lenguajes, frameworks y herramientas.

![formulario](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/9a256461-3c40-4f61-9708-edf084ee993c)

**¿Para qué sirve Visual Studio Code?**

Básicamente, se trata de un editor de código. Esto quiere decir, una herramienta que nos permite editar el texto plano de los archivos de código para programación. Sin embargo, detrás de esa necesidad inicial, Visual Studio Code se puede configurar para realizar muchos tipos de tareas, incluso más allá de abrir y escribir simples archivos de texto.

Así pues, VSCode es una herramienta extremadamente versátil, capaz de facilitar muchas tareas de la programación, llegando (con las correspondientes extensiones) a funcionar casi al nivel de un IDE. Ahora resumimos algunas de sus principales funciones.

**Ventajas clave de utilizar Visual Studio Code**

Al explorar las funcionalidades de Visual Studio Code, hemos dejado entrever algunas de sus ventajas, pero queremos insistir en algunos puntos:

1. Eficiencia y agilidad en la programación.
2. Amplia compatibilidad con lenguajes y frameworks.
3. Potentes herramientas de depuración y pruebas.
4. Integración nativa con Git y control de versiones.
5. Personalización y extensibilidad para adaptarse a tus necesidades.

# POSTMAN

Postman es una herramienta esencial para nuestro proyecto ya que su interfaz de usuario intuitiva y su diseño centrado en el usuario facilitan la creación, prueba y depuración de APIs de manera eficiente. Además, su capacidad para organizar solicitudes en colecciones nos permite mantener nuestras pruebas y desarrollar una API de manera organizada y estructurada. La capacidad de Postman para realizar pruebas automatizadas nos ayuda a garantizar la calidad y estabilidad de nuestra API, identificando rápidamente cualquier problema o error durante el desarrollo.

Es una herramienta que facilita la colaboración y el desarrollo al permitir a los programadores interactuar y evaluar el funcionamiento de servicios web y aplicaciones. Ofrece una interfaz gráfica intuitiva y amigable que simplifica el envío de solicitudes a servidores web y la recepción de las respuestas correspondientes.

Con esta plataforma, es posible administrar varios entornos de desarrollo, organizar las solicitudes en colecciones y llevar a cabo pruebas automatizadas para comprobar el comportamiento de los sistemas. Los desarrolladores utilizan Postman para probar colecciones y catálogos de APIs tanto en el front-end como en el back-end, gestionar el ciclo de vida de las APIs, fomentar el trabajo colaborativo y mejorar la organización del proceso de diseño y desarrollo.

![server-client](https://github.com/sergioarcila99/Implementacion-de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API/assets/163569059/e9f45491-08b4-46da-a84f-923fae1c5b23)

*Tomado de:* https://modest-payne-93a7eb.netlify.app/blog/start-postman-series-1/

**Cómo funciona Postman**

Este entorno ofrece una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y a gestionar las respuestas recibidas.

**Las principales características y funcionalidades de Postman son:**

- **Envío de solicitudes:** Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
- **Gestión de entornos:** Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).
- **Colecciones de solicitudes:** Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
- **Pruebas automatizadas:** Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
- **Documentación de API:** Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.

   # BIBLIOGRAFIA
**Replica set:** https://www.mongodb.com/docs/manual/replication/#additional-features

**Visual Studio Code:** https://www.arsys.es/blog/que-es-visual-studio-code-y-cuales-son-sus-ventajas

**Flask:** https://openwebinars.net/blog/que-es-flask/

**Framework:** https://assemblerinstitute.com/blog/framework-programacion/

**Restful API:** https://platzi.com/clases/1638-api-rest/21611-que-significa-rest-y-que-es-una-api-restful/

**Postman:** https://formadoresit.es/que-es-postman-cuales-son-sus-principales-ventajas/

**Rest:** https://aws.amazon.com/es/what-is/restful-api/#:~:text=La%20transferencia%20de%20estado%20representacional,una%20red%20compleja%20como%20Internet.
