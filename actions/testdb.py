# Ce code est utilisé pour extraire les informations de la base de données en exécutant des requêtes SQL.



import psycopg2
from psycopg2 import Error
import datetime


def connect():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            host="localhost",
            database="chatbot",
            user="postgres",
            password="mounir",
            port="5433"
        )

        # Get cursor
        cur = conn.cursor()
        return cur
    except:
        return False

def medication(name):
    # try:
    #     connection = psycopg2.connect(
    #         database="chatbot",
    #         user="postgres",
    #         password="mounir",
    #         host="localhost", 
    #         port="5433",  
    #     )
    #     print('connection established')
    today = datetime.datetime.now().date()
    # Getting medication start and end date for Antoine:
    query = f'''
            select medication_name, dosage, schedule_time
            from elderlyusers e 
            join medications m
            on e.user_id = m.user_id
            where first_name = '{name}'
            ;
            '''
    try:
        cursor = connect()
        cursor.execute(query)
        print("Query executed successfully.")
        data = cursor.fetchall()
        medicament = data[0][0]
        dosage = data[0][1]
        temps = data[0][2]
        return medicament, temps
    except (Exception, Error) as e:
        print(f"Error: {e}") 




def get_apppointment(name):
    q = f"""
        select appointment_type, appointment_date, appointment_time, location
        from elderlyusers e 
        join appointments a
        on e.user_id = a.user_id
        where first_name = '{name}'
        ;
        """
    cur = connect()
    if cur:
        try:
            cur.execute(q)
            data = cur.fetchall()
        except (Exception, Error) as e:
            print('error executing the query')
            print(e)
            data=[]
    else:
        print('database connection error')
        data=[]
    return data

def get_activity(name):
    q = f"""
        select activity_name, schedule_date, schedule_time, location
        from elderlyusers e 
        join activities a
        on e.user_id = a.user_id
        where first_name = '{name}'
        ;
        """
    cur = connect()
    if cur:
        try:
            cur.execute(q)
            data = cur.fetchall()
        except (Exception, Error) as e:
            print('error executing the query')
            print(e)
            data=[]
    else:
        print('database connection error')
        data=[]
    return data




def get_meal(name):
    q = f"""
        select meal_name, meal_time
                from elderlyusers e 
                join meals m
                on e.user_id = m.user_id
                where first_name = '{name}'
        ;
        """
    cur = connect()
    if cur:
        try:
            cur.execute(q)
            data = cur.fetchall()
            data = data[0]
        except (Exception, Error) as e:
            print('error executing the query')
            print(e)
            data=[]
    else:
        print('database connection error')
        data=[]
    return data

# if __name__=='__main__':
#     print('program running')
#     print(get_activity('Antoine'))