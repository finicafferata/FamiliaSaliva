import streamlit as st
from datetime import datetime
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///ventas.db')

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the model
class Venta(Base):
    __tablename__ = 'ventas'
    
    id = Column(Integer, primary_key=True)
    fecha = Column(Date)
    apies = Column(String(10))
    estacion_eess = Column(String(100))
    codigo_producto = Column(String(10))
    descripcion_producto = Column(String(100))
    venta = Column(String(50))
    volumen = Column(Float)
    um_volumen = Column(String(20))
    precio_unitario = Column(Float)
    monto_bruto = Column(Float)
    comision = Column(Float)
    porcentaje_comision = Column(Float)
    total_liquidar = Column(Float)
    fecha_facturacion = Column(Date)
    fecha_vencimiento = Column(Date)
    rx = Column(String(20))
    created_at = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)

def insert_data(data):
    """Insert data into the database"""
    try:
        session = Session()
        venta = Venta(**data)
        session.add(venta)
        session.commit()
        session.close()
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