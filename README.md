# Sistema de Carga de Datos - Ventas YPF

Aplicación web desarrollada con Streamlit para la carga y gestión de datos de ventas de YPF.

## Características

- Interfaz de usuario intuitiva para carga de datos
- Cálculos automáticos de montos y comisiones
- Almacenamiento en base de datos PostgreSQL
- Validación de datos en tiempo real

## Requisitos

- Python 3.8+
- PostgreSQL
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_DIRECTORIO]
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
Crear un archivo `.env` con las siguientes variables:
```
DB_HOST=localhost
DB_NAME=tu_base_de_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_PORT=5432
```

4. Crear la base de datos:
Ejecutar el script `create_table.sql` en tu base de datos PostgreSQL.

## Uso

1. Iniciar la aplicación:
```bash
streamlit run app.py
```

2. Acceder a la aplicación en el navegador:
```
http://localhost:8501
```

## Estructura del Proyecto

- `app.py`: Aplicación principal de Streamlit
- `create_table.sql`: Script SQL para crear la estructura de la base de datos
- `requirements.txt`: Lista de dependencias de Python
- `.env`: Archivo de configuración de variables de entorno (no incluido en el repositorio)

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request 