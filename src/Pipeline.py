import Utileria as ut
from data import load_data
from data import transformaciones
from models import particle_swarm as ps


class Control:

    def CargarBase(self):
        load_data.main()
        return

    def Transform(self):
        str_query = "SELECT * FROM raw.fuerza_ventas"
        df_Trabajo = ut.get_data(str_query)
        df_Grafos = transformaciones.generar_grafo(df_Trabajo)
        df_Grafos.to_csv('grafos_fza_ventas.csv', index=False, header=True)

        conn = ut.CrearConexionRDS()
        data_file = open('grafos_fza_ventas.csv', "r")
        ut.InsertarEnRDSDesdeArchivo(conn, data_file, 'trabajo.grafos')

        # Aquí hay que agregar un código para eliminar el csv temporal
        return

    def CalcularRutasSeq(self):

        str_Query = 'select distinct(id_fza_ventas) as id_fza_ventas \
                     from trabajo.grafos'
        df_Fza_Ventas = ut.get_data(str_Query)

        # Definición de hiperparámetros de PS
        dict_Hiper_PS = {'Iteraciones': 10,
                         'Particulas': 10,
                         'Alfa': .9,
                         'Beta': 1
                         }

        for fza_ventas in df_Fza_Ventas.id_fza_ventas:
            print('--fza_ventas: ', fza_ventas)
            grafo = []
            df_Fza_Ventas = None
            str_Query = 'select id_origen, id_destino, distancia \
                         from trabajo.grafos where id_fza_ventas = {};'
            df_Fza_Ventas = ut.get_data(str_Query.format(fza_ventas))

            # Ejecución de ambos algoritmos
            obj_PS = self.EjecutarAlgoritmo('PS', df_Fza_Ventas, dict_Hiper_PS)
            # obj_SA = self.EjecutarAlgoritmo('SA', grafo, dict_Hiper_PS)

            # Guardamos la ruta
            self.GuardarRuta(fza_ventas, 'PS', obj_PS.lst_MejorCamino, obj_PS.nbr_MejorCosto)
            # self.GuardarRuta(fza_ventas, 'SA', obj_SA.lst_MejorCamino, obj_SA.nbr_MejorCosto)

        return

    def EjecutarAlgoritmo(self, par_Algoritmo, par_Datos, par_Hiper):

        if par_Algoritmo == 'PS':

            # Se instancia el objeto
            PS = ps.ParticleSwarm(par_Datos, par_Hiper)

            # Ejecución de particle swarm
            PS.Ejecutar()

            return PS

        elif par_Algoritmo == 'SA':

            x = 1

            return x

    def GuardarRuta(self, par_fza_ventas, par_Algorirmo, par_Camino, par_Costo):

        str_Nodos = [str(nodo) for nodo in par_Camino]
        str_Nodos = ", ".join(str_Nodos)
        str_Insert = "insert into trabajo.resultados values \
                      ({},'{}','{}',{})".format(par_fza_ventas,
                                                par_Algorirmo,
                                                str_Nodos,
                                                par_Costo)
        conn = ut.CrearConexionRDS()
        ut.EjecutarQuery(conn, str_Insert)

        return


if __name__ == "__main__":

    # El siguiente objeto, contiene el pipeline principal para:
    # Crear y cargar la base de datos
    # Transormar los datos a un formato adecuado de trabajo
    # Calcular las rutas de todas las fuerzas de ventas de manera secuencial
    objControl = Control()

    objControl.CargarBase()
    objControl.Transform()
    objControl.CalcularRutasSeq()
