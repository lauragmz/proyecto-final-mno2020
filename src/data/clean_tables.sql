DROP TABLE IF EXISTS trabajo.nodos;
CREATE TABLE IF NOT EXISTS trabajo.nodos AS(
  SELECT
  substring(id_nodo  from '[^.]*')::int as nodo,
  lat, lon
  FROM  trabajo.nodos_aux
);

DROP TABLE IF EXISTS trabajo.nodos_aux;
