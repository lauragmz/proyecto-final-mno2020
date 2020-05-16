from src.db_utils import get_data
import pandas as pd
import folium

class ShortestPath:
    """
    Clase con métodos llamados desde la clase "app.py"
    Tiene los métodos para extraer la tabla de sql y crea mapas.
    """
    def get_coordinates_list(self, ruta):
        coordenadas = []
        for nodo in ruta:
            query = "SELECT * FROM trabajo.nodos \
            WHERE nodo = %s ;" % (str(nodo))
            nodo_info = get_data(query)
            coordenadas.append([nodo_info['lat'][0], \
             nodo_info['lon'][0]])
        return coordenadas

    def create_map(self, coordenadas, map_name):
        centros = pd.DataFrame(coordenadas)
        centros.columns = ['lat', 'lon']
        #Definición de punto: Oficina de servicio
        os = centros.loc[[0], ['lat', 'lon']].values.tolist()

        cen_lon = centros.lon.mean()
        cen_lat = centros.lat.mean()
        mapi = folium.Map(location=[cen_lat,cen_lon],
                          zoom_start = 12,
                          tiles= "OpenStreetMap")
        folium.PolyLine(coordenadas + [coordenadas[0]],
                        color='red',
                        weight=2,
                        opacity=0.8).add_to(mapi)
        folium.Marker(os[0], icon=folium.Icon(color='blue', icon='cloud') ).add_to(mapi)

        mapi.save(map_name)


    def get_path(self, algorithm, fza_ventas, map_name):
        try:
            if algorithm  ==  int(1):
                query = "SELECT * FROM trabajo.resultados WHERE algoritmo = 'SA' \
                 AND id_fza_ventas = %s ;" % (str(fza_ventas))
                df = get_data(query)
                ruta = df['ruta_optima'][0].split(',')
                print(ruta)
                coordenadas = self.get_coordinates_list(ruta)

                self.create_map(coordenadas, map_name)
                distancia = df['distancia'][0]

            return distancia
        except (Exception) as error :
            print ("Error while getting path", error)

    def get_distance(self, algorithm, fza_ventas):
        try:
            if algorithm  ==  int(1):
                query = "SELECT * FROM trabajo.resultados WHERE algoritmo = 'SA' \
                 AND id_fza_ventas = %s ;" % (str(fza_ventas))
                df = get_data(query)
                distancia = df['distancia'][0]

            return distancia
        except (Exception) as error :
            print ("Error while getting path", error)

#agent = ShortestPath()
#agent.get_path(1, 124)
