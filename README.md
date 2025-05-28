# Sistema de Carga de Datos - Ventas YPF

Aplicación web desarrollada con Streamlit para la carga y gestión de datos de ventas de YPF.

## Características

- Interfaz de usuario intuitiva para carga de datos
- Cálculos automáticos de montos y comisiones
- Almacenamiento en base de datos SQLite (compatible con Streamlit Cloud)
- Validación de datos en tiempo real

## Requisitos

- Python 3.8+
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

3. Configurar variables de entorno (opcional):
Crear un archivo `.env` con las siguientes variables:
```
DATABASE_URL=sqlite:///ventas.db
```

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
- `requirements.txt`: Lista de dependencias de Python
- `.env`: Archivo de configuración de variables de entorno (opcional)

## Deployment en Streamlit Cloud

La aplicación está configurada para funcionar directamente en Streamlit Cloud sin necesidad de configuración adicional. Los datos se almacenan en una base de datos SQLite.

## Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request 