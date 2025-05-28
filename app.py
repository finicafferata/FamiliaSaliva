import streamlit as st
import sqlite3
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration
DB_PATH = os.getenv('DB_PATH', 'ventas.db')

def init_db():
    """Initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    # Create table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha DATE,
            apies TEXT,
            estacion_eess TEXT,
            codigo_producto TEXT,
            descripcion_producto TEXT,
            venta TEXT,
            volumen REAL,
            um_volumen TEXT,
            precio_unitario REAL,
            monto_bruto REAL,
            comision REAL,
            porcentaje_comision REAL,
            total_liquidar REAL,
            fecha_facturacion DATE,
            fecha_vencimiento DATE,
            rx TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_data(data):
    """Insert data into the database"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        query = '''
        INSERT INTO ventas (
            fecha, apies, estacion_eess, codigo_producto, descripcion_producto,
            venta, volumen, um_volumen, precio_unitario, monto_bruto,
            comision, porcentaje_comision, total_liquidar, fecha_facturacion,
            fecha_vencimiento, rx
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        
        values = (
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
        )
        
        c.execute(query, values)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error inserting data: {str(e)}")
        return False

def calculate_values(volumen, precio_unitario, porcentaje_comision):
    """Calculate derived values"""
    monto_bruto = volumen * precio_unitario
    comision = monto_bruto * (porcentaje_comision / 100)
    total_liquidar = monto_bruto + comision
    return monto_bruto, comision, total_liquidar

def main():
    # Initialize database
    init_db()
    
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