import Utileria as ut
import pandas as pd


def generar_grafo(df_Fzas_de_Ventas):

    list_fza_ventas = df_Fzas_de_Ventas.fza_ventas.unique().tolist()

    # cnn = ut.CrearConexionRDS()

    datos_Totales = []
    for fza_venta in list_fza_ventas:
        # print('fza_venta: ', fza_venta)
        dm, df2 = ut.distance_matrix(df_Fzas_de_Ventas, fza_venta)
        datos_FzaVenta = []
        for fila in dm:
            # str_Query = "INSERT INTO TRABAJO.GRAFOS VALUES ({0},'{1}',{2},{3},{4})"
            # print(str_Query.format(fza_venta, 'tmp', fila[0], fila[1], fila[2]))
            # ut.EjecutarQuery(cnn, str_Query.format(fza_venta, 'tmp', fila[0], fila[1], fila[2]))
            datos_FzaVenta = [fza_venta, 'tmp', fila[0], fila[1], fila[2]]
            datos_Totales.append(datos_FzaVenta)

    data = datos_Totales

    df_Resultado = pd.DataFrame(data, columns=['id_fza_venta',
                                           'estado',
                                           'origen',
                                           'destino',
                                           'distancia'])

    # df_Resultado['origen'] -= 1
    # df_Resultado['destino'] -= 1

    return df_Resultado
