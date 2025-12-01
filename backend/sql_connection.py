import psycopg2

__conn = None

def get_sql_connection():
    global __conn
    if __conn is None:
        __conn = psycopg2.connect(
                host="localhost",
                database="employeedb",   # ✅ your actual database
                user="postgres",         # default superuser
                password="2004"  # replace with the real password
            )
    return __conn