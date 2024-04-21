# Metodologia de-un-Crud-con-Python-Flask-MongoDB-y-RestFul-API

MongoDB es una base de datos flexible y potente que permite una amplia variedad de enfoques para modelar datos y realizar consultas. A continuación, te presento algunos principios y prácticas comunes que se suelen seguir al trabajar con MongoDB:

**Modelado de Datos Orientado a Documentos:** En MongoDB, los datos se almacenan en documentos BSON (JSON binario) en lugar de en filas y columnas como en las bases de datos relacionales. Por lo tanto, es importante diseñar el esquema de la base de datos teniendo en cuenta la estructura de los documentos y cómo se van a acceder y manipular los datos.

**Normalización vs. Denormalización:** A diferencia de las bases de datos relacionales, en MongoDB se puede optar por normalizar o denormalizar los datos según las necesidades del caso de uso. La denormalización puede mejorar el rendimiento al reducir la necesidad de realizar operaciones de unión, pero puede aumentar el tamaño de los documentos.

**Índices Eficientes:** MongoDB admite la creación de índices para mejorar el rendimiento de las consultas. Es importante identificar las consultas frecuentes y crear índices adecuados para ellas. Sin embargo, demasiados índices pueden afectar el rendimiento de las operaciones de escritura.

**Sharding para Escalabilidad Horizontal:** MongoDB ofrece la capacidad de escalar horizontalmente a través del sharding, que distribuye los datos en múltiples servidores. Esto permite manejar grandes volúmenes de datos y aumentar la capacidad de lectura y escritura.

**Transacciones:** A partir de la versión 4.0, MongoDB ofrece soporte para transacciones ACID en ciertos casos de uso, lo que permite realizar operaciones de lectura y escritura en varias colecciones de manera atómica.

**Seguridad:** MongoDB proporciona varias características de seguridad, como autenticación, autorización, encriptación de datos en reposo y en tránsito, y auditoría de eventos. Es importante configurar adecuadamente la seguridad para proteger los datos sensibles.

**Resiliencia y Tolerancia a Fallos:** MongoDB ofrece opciones de configuración para garantizar la resiliencia y la tolerancia a fallos, como la replicación automática y la detección de nodos de manera automática.

**Monitorización y Optimización de Rendimiento:** Es importante monitorear el rendimiento del clúster de MongoDB y optimizarlo según sea necesario. Herramientas como MongoDB Compass y MongoDB Cloud Manager pueden ayudar en la monitorización y la optimización del rendimiento.
