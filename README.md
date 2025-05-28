# Sistema de Carga de Datos

Aplicación Streamlit para la carga de datos en dos tablas PostgreSQL: RX y Playa.

## Características

- Interfaz de usuario intuitiva con Streamlit
- Dos formularios separados para carga de datos RX y Playa
- Validación de campos obligatorios
- Conexión a base de datos PostgreSQL
- Mensajes de confirmación al guardar datos
- Navegación mediante sidebar

## Requisitos

- Python 3.8+
- PostgreSQL
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Crear y activar entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
   - Copiar `.env.example` a `.env`
   - Modificar las variables con los datos de tu base de datos

5. Crear las tablas en PostgreSQL:
```bash
psql -U tu_usuario -d tu_base_de_datos -f create_tables.sql
```

## Uso

1. Iniciar la aplicación:
```bash
streamlit run app.py
```

2. Abrir el navegador en la URL mostrada (generalmente http://localhost:8501)

3. Usar el menú lateral para navegar entre los formularios de carga

## Estructura del Proyecto

- `app.py`: Aplicación principal
- `create_tables.sql`: Script SQL para crear las tablas
- `requirements.txt`: Dependencias del proyecto
- `.env`: Variables de entorno (no incluido en el repositorio)
- `.env.example`: Ejemplo de variables de entorno 