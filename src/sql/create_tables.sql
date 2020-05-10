/***********************************************************************************/
/**************************** Preparacion de las tablas ****************************/
/***********************************************************************************/


/**************************** trabajo grafos ****************************/
drop table if exists trabajo.grafos;
create table trabajo.grafos (
  id_fza_ventas NUMERIC,
  estado VARCHAR(30),
  id_origen NUMERIC,
  id_destino NUMERIC,
  distancia numeric
);
comment on table trabajo.grafos is 'Grafos de rutas de las fuerzas de venta';

/**************************** trabajo resultados Particle swarm ****************************/
drop table if exists trabajo.resultados_ps;
create table trabajo.resultados_ps (
  id_fza_ventas NUMERIC,
  estado VARCHAR(30),
  ruta_optima varchar(100),
  distancia numeric
);
comment on table trabajo.resultados_ps is 'Resultados del algoritmo Particle Swarm';

/**************************** trabajo resultados Simulated Annealing ****************************/
drop table if exists trabajo.resultados_sa;
create table trabajo.resultados_sa (
  id_fza_ventas NUMERIC,
  estado VARCHAR(30),
  ruta_optima varchar(100),
  distancia numeric
);
comment on table trabajo.resultados_sa is 'Resultados del algoritmo Simulated Annealing';

/**************************** trabajo mapeo de nodos y coordenadas ****************************/
drop table if exists trabajo.catalogo_nodos;
create table trabajo.catalogo_nodos (
  id_nodo varchar(10),
  latitud numeric,
  longitud numeric
);
comment on table trabajo.catalogo_nodos is 'Catálogo de nodos y coordenadas';
