from io import StringIO
import psycopg2
import pandas as pd


def save_rds(df,table_name):

    # Copy to postgres
    connection = psycopg2.connect(user=MY_USER , # Usuario RDS
                                 password=MY_PASS, # password de usuario de RDS
                                 host=MY_HOST,#"127.0.0.1", # cambiar por el endpoint adecuado
                                 port=MY_PORT, # cambiar por el puerto
                                 database=MY_DB) # Nombre de la base de datos
    cursor = connection.cursor()

    records = df.values.tolist()
    buffer = StringIO()
    for line in records:
        buffer.write('~'.join([str(x) for x in line]) + '\n')

    buffer.seek(0)

    cursor.copy_from(buffer, table_name, null='NaN', sep ='~' )
    connection.commit()
    cursor.close()
    connection.close()

def execute_sql(file_dir):
    """ Sirve para ejecutar archivos .sql """
    try:
        connection = psycopg2.connect(user=MY_USER , # Usuario RDS
                                     password=MY_PASS, # password de usuario de RDS
                                     host=MY_HOST,#"127.0.0.1", # cambiar por el endpoint adecuado
                                     port=MY_PORT, # cambiar por el puerto
                                     database=MY_DB) # Nombre de la base de datos
        cursor = connection.cursor()

        print(file_dir)
        cursor.execute(open(file_dir, "r").read())
        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.Error) as error :
        print ("Error while executing sql file", error)

def main():
    file_dir = "create_tables.sql"
    execute_sql(file_dir)

    file_name = "./../../data/raw/raw.csv"
    df = pd.read_csv(file_name, encoding = "latin-1")
    save_rds(df, "trabajo.fuerza_ventas")

    file_name = "./../../data/raw/base_nodos.csv"
    df = pd.read_csv(file_name)
    save_rds(df, "trabajo.nodos_aux")

    file_dir = "clean_tables.sql"
    execute_sql(file_dir)


main()
