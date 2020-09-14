import psycopg2
from config import *


try:
    conn = psycopg2.connect(
        dbname=DB_DATABASE,
        user=DB_USER,
        password=DB_PASS,
        host=DB_SERVER,
        port=DB_PORT,
    )
    cur = conn.cursor()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)

