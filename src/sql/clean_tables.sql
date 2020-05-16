drop table if exists trabajo.nodos
create table trabajo.nodos as(
    select
    substring(id_nodo  from '[^.]*')::int as nodo,
    lat, lon
    from trabajo.catalogo_nodos
);
comment on table trabajo.catalogo_nodos is 'Catálogo de nodos y coordenadas sin comillas en id_nodo';

drop table if exists trabajo.catalogo_nodos;

