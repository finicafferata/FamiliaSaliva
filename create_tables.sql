-- Tabla para datos RX
CREATE TABLE rx_data (
    id SERIAL PRIMARY KEY,
    copetrol VARCHAR(50),
    fecha DATE NOT NULL,
    producto VARCHAR(100) NOT NULL,
    litros DECIMAL(10,2) NOT NULL,
    importe DECIMAL(10,2) NOT NULL,
    forma_de_pago VARCHAR(50) NOT NULL,
    cuil VARCHAR(20),
    dni VARCHAR(20),
    dominio VARCHAR(20),
    km INTEGER,
    apellido_y_nombre VARCHAR(200),
    observaciones TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla para datos Playa
CREATE TABLE playa_data (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    turno VARCHAR(50) NOT NULL,
    nombre VARCHAR(100),
    horario VARCHAR(50),
    producto VARCHAR(100) NOT NULL,
    stock_inicial DECIMAL(10,2),
    venta DECIMAL(10,2) NOT NULL,
    precio DECIMAL(10,2),
    total DECIMAL(10,2) NOT NULL,
    reposicion DECIMAL(10,2),
    stock_final DECIMAL(10,2),
    obs TEXT,
    obs_playa TEXT,
    dif DECIMAL(10,2),
    tarj DECIMAL(10,2),
    efectivo DECIMAL(10,2),
    total_declarado DECIMAL(10,2),
    firmado BOOLEAN DEFAULT FALSE,
    obs_cierre TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 