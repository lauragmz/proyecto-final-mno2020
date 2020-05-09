"""
Archivo con utilidades para utilizar el CoupledAnnealer
"""

import pandas as pd
import math
import random
from pycsa import CoupledAnnealer

try:
    xrange
except NameError:
    xrange = range
    
def diccionario_lugares(df,fv):
    """
    Función para generar un diccinario con los lugares que visita una fuerza de venta.
    Args:
        df (dataFrame): DataFrame con la base de datos
        fv (int): Fuerza de venta del que queremos generar el diccionario.
    Returns:
        lugares(diccionario): incluye los puntos que debe visitar con sus coordenas. 
    """
    df2 = df[(df.fza_ventas == fv)]
    df2['lugar'] = range(1, len(df2) + 1)
    df2 = df2.append({'lugar' : 'base' , 'lat_destino' : df2.iloc[0]['lat_origen'],'lon_destino': df2.iloc[0]['lon_origen'] } , ignore_index=True)
    df3 = df2[['lugar','lat_destino','lon_destino']].copy()
    lugares = {a:(b,c)for a, b, c in df3.values}
    return lugares

    
def distance(a, b):
    """
    Helper function to calculate the distance between two 
    latitude-longitude coordinates.
    """
    R = 6371  # radius of Earth (miles)
    lat1, lon1 = math.radians(a[0]), math.radians(a[1])
    lat2, lon2 = math.radians(b[0]), math.radians(b[1])
    return math.acos(math.sin(lat1) * math.sin(lat2) +
                     math.cos(lat1) * math.cos(lat2) * 
                     math.cos(lon1 - lon2)) * R

# Create the distance matrix between the cities.
def get_distance_matrix(lugares):
    distance_matrix = {}
    for ka, va in lugares.items():
        distance_matrix[ka] = {}
        for kb, vb in lugares.items():
            if kb == ka:
                distance_matrix[ka][kb] = 0.0
            else:
                distance_matrix[ka][kb] = distance(va, vb)
    return distance_matrix
            
            
def get_inits(df, fv):
    lugares = diccionario_lugares(df,fv)
    distance_matrix = get_distance_matrix(lugares)
    
    init_state = list(lugares.keys())
    
    def get_probe(positions, tgen):
        """
        Swap two cities in the route.

        Note that `tgen` (the generation temperature) is ignored here.
        In general, you can use `tgen` to adjust the variance of
        the probing jumps as the algorithm progress.
        """
        a = random.randint(0, len(positions) - 1)
        b = random.randint(0, len(positions) - 1)
        positions[a], positions[b] = positions[b], positions[a]
        return positions


    def get_target(positions):
        """
        Calculates the length of the route.
        """
        e = 0
        for i in xrange(len(positions)):
            e += distance_matrix[positions[i-1]][positions[i]]
        return e
    
    return get_probe, get_target, init_state