import psycopg2
from psycopg2 import sql

# Configuración de la conexión
DB_CONFIG = {
    'host': 'dpg-cu1apb52ng1s73e9q9kg-a',  # Reemplaza con el host de tu base de datos
    'database': 'sistema_matricula_inar',   # Reemplaza con el nombre de tu base de datos
    'user': 'sistema_matricula_inar_user',  # Reemplaza con tu usuario
    'password': 'VQLXylYznZN5QDFTtR7uGSL4T5eTlKBf',           # Reemplaza con tu contraseña
    'port': 5432                           # El puerto por defecto de PostgreSQL
}

try:
    # Conexión a la base de datos
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    print("Conexión exitosa a la base de datos.")

    # Crear tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')
    conn.commit()
    print("Tabla 'usuarios' creada correctamente.")

    # Insertar datos
    cursor.execute('''
        INSERT INTO usuarios (nombre, email)
        VALUES (%s, %s)
    ''', ('Juan Pérez', 'juan.perez@example.com'))
    conn.commit()
    print("Datos insertados correctamente.")

    # Consultar datos
    cursor.execute('SELECT * FROM usuarios;')
    rows = cursor.fetchall()
    print("Datos en la tabla 'usuarios':")
    for row in rows:
        print(row)

except psycopg2.Error as e:
    print(f"Error al trabajar con la base de datos: {e}")

finally:
    # Cerrar la conexión
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Conexión cerrada.")
