import streamlit as st
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Database connection parameters
DB_PARAMS = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'dbname': os.getenv('DB_NAME', 'your_database'),
    'user': os.getenv('DB_USER', 'your_username'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
    'port': os.getenv('DB_PORT', '5432')
}

def create_connection():
    """Create a database connection"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        return conn
    except psycopg2.OperationalError as e:
        st.error(f"Error de conexión a la base de datos: {str(e)}")
        st.error("Por favor, verifica que las variables de entorno estén configuradas correctamente.")
        return None
    except Exception as e:
        st.error(f"Error inesperado: {str(e)}")
        return None

def insert_rx_data(data):
    """Insert data into rx_data table"""
    conn = create_connection()
    if conn is None:
        return False
    
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO rx_data (
            copetrol, fecha, producto, litros, importe, forma_de_pago,
            cuil, dni, dominio, km, apellido_y_nombre, observaciones
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            data['copetrol'],
            data['fecha'],
            data['producto'],
            data['litros'],
            data['importe'],
            data['forma_de_pago'],
            data['cuil'],
            data['dni'],
            data['dominio'],
            data['km'],
            data['apellido_y_nombre'],
            data['observaciones']
        ))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error inserting data: {str(e)}")
        if conn:
            conn.close()
        return False

def insert_playa_data(data):
    """Insert data into playa_data table"""
    conn = create_connection()
    if conn is None:
        return False
    
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO playa_data (
            fecha, turno, nombre, horario, producto, stock_inicial,
            venta, precio, total, reposicion, stock_final, obs,
            obs_playa, dif, tarj, efectivo, total_declarado,
            firmado, obs_cierre
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            data['fecha'],
            data['turno'],
            data['nombre'],
            data['horario'],
            data['producto'],
            data['stock_inicial'],
            data['venta'],
            data['precio'],
            data['total'],
            data['reposicion'],
            data['stock_final'],
            data['obs'],
            data['obs_playa'],
            data['dif'],
            data['tarj'],
            data['efectivo'],
            data['total_declarado'],
            data['firmado'],
            data['obs_cierre']
        ))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error inserting data: {str(e)}")
        if conn:
            conn.close()
        return False

def rx_form():
    """Form for RX data entry"""
    st.subheader("Carga RX")
    
    with st.form("rx_form"):
        # Form fields
        copetrol = st.text_input("COPETROL")
        fecha = st.date_input("FECHA *", value=datetime.now())
        producto = st.text_input("PRODUCTO *")
        litros = st.number_input("LITROS *", min_value=0.0, step=0.01)
        importe = st.number_input("IMPORTE *", min_value=0.0, step=0.01)
        forma_de_pago = st.selectbox("FORMA DE PAGO *", ["EFECTIVO", "TARJETA", "TRANSFERENCIA"])
        cuil = st.text_input("CUIL")
        dni = st.text_input("DNI")
        dominio = st.text_input("DOMINIO")
        km = st.number_input("KM", min_value=0)
        apellido_y_nombre = st.text_input("APELLIDO Y NOMBRE")
        observaciones = st.text_area("OBSERVACIONES")
        
        # Submit button
        submitted = st.form_submit_button("Guardar")
        
        if submitted:
            # Validate required fields
            if not all([fecha, producto, litros, importe, forma_de_pago]):
                st.error("Por favor complete todos los campos obligatorios (*)")
                return
            
            # Prepare data dictionary
            data = {
                'copetrol': copetrol,
                'fecha': fecha,
                'producto': producto,
                'litros': litros,
                'importe': importe,
                'forma_de_pago': forma_de_pago,
                'cuil': cuil,
                'dni': dni,
                'dominio': dominio,
                'km': km,
                'apellido_y_nombre': apellido_y_nombre,
                'observaciones': observaciones
            }
            
            # Insert data
            if insert_rx_data(data):
                st.success("¡Datos guardados exitosamente!")
            else:
                st.error("Error al guardar los datos")

def playa_form():
    """Form for Playa data entry"""
    st.subheader("Carga Playa")
    
    with st.form("playa_form"):
        # Form fields
        fecha = st.date_input("FECHA *", value=datetime.now())
        turno = st.selectbox("TURNO *", ["MAÑANA", "TARDE", "NOCHE"])
        nombre = st.text_input("NOMBRE")
        horario = st.text_input("HORARIO")
        producto = st.text_input("PRODUCTO *")
        stock_inicial = st.number_input("STOCK INICIAL", min_value=0.0, step=0.01)
        venta = st.number_input("VENTA *", min_value=0.0, step=0.01)
        precio = st.number_input("PRECIO", min_value=0.0, step=0.01)
        total = st.number_input("TOTAL *", min_value=0.0, step=0.01)
        reposicion = st.number_input("REPOSICIÓN", min_value=0.0, step=0.01)
        stock_final = st.number_input("STOCK FINAL", min_value=0.0, step=0.01)
        obs = st.text_area("OBS")
        obs_playa = st.text_area("OBS PLAYA")
        dif = st.number_input("DIF", step=0.01)
        tarj = st.number_input("TARJ", min_value=0.0, step=0.01)
        efectivo = st.number_input("EFECTIVO", min_value=0.0, step=0.01)
        total_declarado = st.number_input("TOTAL DECLARADO", min_value=0.0, step=0.01)
        firmado = st.checkbox("FIRMADO")
        obs_cierre = st.text_area("OBS CIERRE")
        
        # Submit button
        submitted = st.form_submit_button("Guardar")
        
        if submitted:
            # Validate required fields
            if not all([fecha, turno, producto, venta, total]):
                st.error("Por favor complete todos los campos obligatorios (*)")
                return
            
            # Prepare data dictionary
            data = {
                'fecha': fecha,
                'turno': turno,
                'nombre': nombre,
                'horario': horario,
                'producto': producto,
                'stock_inicial': stock_inicial,
                'venta': venta,
                'precio': precio,
                'total': total,
                'reposicion': reposicion,
                'stock_final': stock_final,
                'obs': obs,
                'obs_playa': obs_playa,
                'dif': dif,
                'tarj': tarj,
                'efectivo': efectivo,
                'total_declarado': total_declarado,
                'firmado': firmado,
                'obs_cierre': obs_cierre
            }
            
            # Insert data
            if insert_playa_data(data):
                st.success("¡Datos guardados exitosamente!")
            else:
                st.error("Error al guardar los datos")

def main():
    st.title("Sistema de Carga de Datos")
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Seleccione una opción",
        ["Carga RX", "Carga Playa"]
    )
    
    # Show selected page
    if page == "Carga RX":
        rx_form()
    else:
        playa_form()

if __name__ == "__main__":
    main() 