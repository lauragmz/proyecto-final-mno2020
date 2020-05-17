from io import StringIO
import psycopg2
import pandas as pd

MY_USER = 'postgres'
MY_DB = 'db_mno'
MY_HOST = 'database-rita.cnevbxmlm0lp.us-west-2.rds.amazonaws.com'
MY_PASS = '1234567890'
MY_PORT = 5432

def get_data(query):
    try:
        connection = psycopg2.connect(user=MY_USER , # Usuario RDS
                                     password=MY_PASS, # password de usuario de RDS
                                     host=MY_HOST ,#"127.0.0.1", # cambiar por el endpoint adecuado
                                     port=MY_PORT, # cambiar por el puerto
                                     database=MY_DB ) # Nombre de la base de datos
        cursor = connection.cursor()

        cursor.execute(query)

        #print("Selecting rows from table using cursor.fetchall")
        records = cursor.fetchall()
        df = pd.DataFrame(records)
        col_names =  [i[0] for i in cursor.description]
        df.columns = col_names
        cursor.close()
        connection.close()
        #print("PostgreSQL connection is closed")
        return df

    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)
