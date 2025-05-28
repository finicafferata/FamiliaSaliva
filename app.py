import streamlit as st
import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

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
    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")
        return None

def insert_data(data):
    """Insert data into the database"""
    conn = create_connection()
    if conn is None:
        return False
    
    try:
        cur = conn.cursor()
        query = """
        INSERT INTO ventas (
            fecha, apies, estacion_eess, codigo_producto, descripcion_producto,
            venta, volumen, um_volumen, precio_unitario, monto_bruto,
            comision, porcentaje_comision, total_liquidar, fecha_facturacion,
            fecha_vencimiento, rx
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            data['fecha'],
            data['apies'],
            data['estacion_eess'],
            data['codigo_producto'],
            data['descripcion_producto'],
            data['venta'],
            data['volumen'],
            data['um_volumen'],
            data['precio_unitario'],
            data['monto_bruto'],
            data['comision'],
            data['porcentaje_comision'],
            data['total_liquidar'],
            data['fecha_facturacion'],
            data['fecha_vencimiento'],
            data['rx']
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

def calculate_values(volumen, precio_unitario, porcentaje_comision):
    """Calculate derived values"""
    monto_bruto = volumen * precio_unitario
    comision = monto_bruto * (porcentaje_comision / 100)
    total_liquidar = monto_bruto + comision
    return monto_bruto, comision, total_liquidar

def main():
    st.title("Sistema de Carga de Datos - Ventas YPF")
    
    # Create form
    with st.form("venta_form"):
        st.subheader("Ingrese los datos de la venta")
        
        # Form fields
        col1, col2 = st.columns(2)
        
        with col1:
            fecha = st.date_input("FECHA")
            apies = st.text_input("APIES")
            estacion_eess = st.text_input("ESTACIÓN EESS")
            codigo_producto = st.text_input("CÓDIGO PRODUCTO")
            descripcion_producto = st.text_input("DESCRIPCIÓN PRODUCTO")
            venta = st.selectbox("VENTA", ["SURTIDOR Venta", "APP Venta"])
            volumen = st.number_input("VOLUMEN", min_value=0.0, step=0.01)
            um_volumen = st.text_input("UM (VOLUMEN)", value="Litros")
            
        with col2:
            precio_unitario = st.number_input("PRECIO UNITARIO", min_value=0.0, step=0.01)
            porcentaje_comision = st.number_input("PORCENTAJE DE COMISIÓN", step=0.01)
            fecha_facturacion = st.date_input("FECHA DE FACTURACIÓN")
            fecha_vencimiento = st.date_input("FECHA DE VENCIMIENTO")
            rx = st.text_input("RX")
            
            # Calcular valores automáticamente
            monto_bruto, comision, total_liquidar = calculate_values(
                volumen, precio_unitario, porcentaje_comision
            )
            
            # Mostrar valores calculados
            st.metric("MONTO BRUTO", f"${monto_bruto:,.2f}")
            st.metric("COMISIÓN", f"${comision:,.2f}")
            st.metric("TOTAL A LIQUIDAR", f"${total_liquidar:,.2f}")
        
        # Submit button
        submitted = st.form_submit_button("Guardar")
        
        if submitted:
            # Prepare data dictionary
            data = {
                'fecha': fecha,
                'apies': apies,
                'estacion_eess': estacion_eess,
                'codigo_producto': codigo_producto,
                'descripcion_producto': descripcion_producto,
                'venta': venta,
                'volumen': volumen,
                'um_volumen': um_volumen,
                'precio_unitario': precio_unitario,
                'monto_bruto': monto_bruto,
                'comision': comision,
                'porcentaje_comision': porcentaje_comision,
                'total_liquidar': total_liquidar,
                'fecha_facturacion': fecha_facturacion,
                'fecha_vencimiento': fecha_vencimiento,
                'rx': rx
            }
            
            # Insert data
            if insert_data(data):
                st.success("¡Datos guardados exitosamente!")
            else:
                st.error("Error al guardar los datos")

if __name__ == "__main__":
    main() 