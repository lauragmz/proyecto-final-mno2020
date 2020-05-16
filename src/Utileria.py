from math import radians, cos, sin, asin, sqrt
from dynaconf import settings
from io import StringIO
    
import pandas as pd
import psycopg2
import psycopg2.extras

    
class Utileria():
    '''
    Clase donde se almacenarán las funciones genéricas para la implementación
    de los algoritmos Particle Swarn y Simulated Annealing
    '''

    def calcular_distancia_coord(self, nbr_LongA, nbr_LatA, nbr_LongB, nbr_LatB, str_unidad='km'):
     '''
     Función para calcular la distancia entre coordenadas en la tierra (esfera)
     Recibe las coordenaas del punto A, del punto B y las unidades en las que se realizará el cálculo
     Devuelve la distancia de acuerdo a la unidad especificada (por defecto km)
     '''
        # primero se convierte todo a radianes
        nbr_LongA = radians(nbr_LongA)
        nbr_LatA = radians(nbr_LatA)
        nbr_LongB = radians(nbr_LongB)
        nbr_LatB = radians(nbr_LatB)

        # Aplicamos la fórmula de Haversine
        nbr_delta_lon = nbr_LongB - nbr_LongA
        nbr_delta_lat = nbr_LatB - nbr_LatA
        nbr_a = sin(nbr_delta_lat / 2)**2 + cos(nbr_LatA) * cos(nbr_LatB) * sin(nbr_delta_lon / 2)**2

        nbr_c = 2 * asin(sqrt(nbr_a))

        # Dependiendo del tipo de unidad especificada, sera el valor que usaremos como radio
        # La tierra no es una esfera perfecta, asi que usaremos un radio entre el ecuatorial y el polar
        if str_unidad == 'km':
            nbr_r = 6371
        elif str_unidad == 'miles':
            nbr_r = 3956
        else:
            print('Se especificó una unidad de medición no válida. No es posible realizar el cálculo')
            return 0

        nbr_resultado = nbr_c * nbr_r

        return nbr_resultado



def CrearConexionRDS():
    '''
    '''
    conn = psycopg2.connect(database=settings.get('dbname'),
                                user=settings.get('user'),
                                password=settings.get('password'),
                                host=settings.get('host'),
                                port='5432')
    return conn



def get_data(query):
    '''
    '''
    try:
        connection = CrearConexionRDS()
        cursor = connection.cursor()

        cursor.execute(query)

        print("Selecting rows from table using cursor.fetchall")
        records = cursor.fetchall()
        df = pd.DataFrame(records)
        col_names =  [i[0] for i in cursor.description]
        df.columns = col_names
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        return df

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)



def convert(ruta):
    '''
    '''
    s = [str(i) for i in ruta]
    ruta_c = "-".join(s)
    return(ruta_c)



def ruta(df, fv):
    '''
    '''
    df1 = df[(df.fza_ventas == fv)]
    dfo = df1.filter(['fza_ventas', 'id_origen', 'lat_origen', 'lon_origen'], axis=1).drop_duplicates()
    dfo = dfo.rename({'id_origen': 'id', 'lat_origen': 'lat', 'lon_origen': 'lon'}, axis=1)
    dfd = df1.filter(['fza_ventas', 'no_cliente', 'lat_destino','lon_destino'], axis=1)
    dfd = dfd.rename({'no_cliente': 'id', 'lat_destino': 'lat', 'lon_destino': 'lon'}, axis=1)
    df2 = pd.concat([dfo, dfd])
    df2['posicion'] = 0
    df2['posicion'] = df2.groupby(['posicion']).cumcount()+1
    return df2



def distance_matrix(df, fv):
    '''
    '''
    df2 = ruta(df, fv)
    dm = []
    ut = Utileria()
    for i in range(df2.shape[0]):
        for j in range(i+1, df2.shape[0]):
            d = ut.calcular_distancia_coord(df2.iloc[i, 3], df2.iloc[i, 2],  df2.iloc[j, 3], df2.iloc[j, 2])
            elemento = [df2.iloc[i,4], df2.iloc[j,4], d]
            dm.append(elemento)
    return dm, df2


def split_tolist(string):
    '''
    '''
    li = list(string.split("-"))
    return li



def vis_mapa(df, mejor_ruta):
    '''
    Preparación de datos para creación de mapa
    '''
    import folium

    df=df.set_index('posicion')
    df=df.reindex(mejor_ruta)
    coordenadas = df[['lat', 'lon']].values.tolist()
    os = df.loc[[1], ['lat', 'lon']].values.tolist() #Definición de punto: Oficina de servicio
    cen_lon = df.lon.mean()
    cen_lat = df.lat.mean()
    mapi = folium.Map(location=[cen_lat,cen_lon],
                  zoom_start = 12,
                  tiles="cartodbpositron")
    folium.PolyLine(coordenadas + [coordenadas[0]],
                color='red',
                weight=1,
                opacity=0.8).add_to(mapi)
    folium.Marker(os[0],icon=folium.Icon(color='blue') ).add_to(mapi)

    return mapi
