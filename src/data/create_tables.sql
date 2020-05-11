CREATE SCHEMA IF NOT EXISTS trabajo;

DROP TABLE IF EXISTS trabajo.fuerza_ventas;
CREATE TABLE IF NOT EXISTS trabajo.fuerza_ventas (
  fza_ventas integer,
  no_cliente integer,
  lat_destino real,
  lon_destino real,
  id_origen text,
  estado text,
  lat_origen real,
  lon_origen real
);

DROP TABLE IF EXISTS trabajo.nodos_aux;
CREATE TABLE IF NOT EXISTS trabajo.nodos_aux(
  id_nodo text,
  lat real,
  lon real
);
