import json
import psycopg2
from config import *

# No need to have logging for a standalone file such as this one


def import_json_data(cursor):
    print("Parsing JSON data")
    with open("./products.json") as f:
        data = json.load(f)

    print("Inserting JSON data into database")
    for product in data:
        cursor.execute(
            f"""
                INSERT INTO {DB_PRODUCTS} (id, name, brand, price, stock)
                VALUES(%s, %s, %s, %s, %s);
            """
        , (
                product['id'],
                product['name'],
                product['brand'],
                product['price'],
                product['in_stock_quantity']
             )
        )


def create_tables():
    conn = None

    try:
        print(f"Opening database connection to {DB_DATABASE}...")
        conn = psycopg2.connect(
            dbname=DB_DATABASE,
            user=DB_USER,
            password=DB_PASS,
            host=DB_SERVER,
            port=DB_PORT,
        )
        cur = conn.cursor()
        print(f"Creating table with name: {DB_PRODUCTS}")
        cur.execute(
            f"""
                CREATE TABLE {DB_PRODUCTS} (
                id INT PRIMARY KEY,
                name VARCHAR ( 500 ) NOT NULL,
                brand VARCHAR ( 500 ) NOT NULL,
                price VARCHAR ( 50 ) NOT NULL,
                stock INT NOT NULL
                );
            """
        )

        print(f"Creating table with name: {DB_LIST}")
        cur.execute(
            f"""
                CREATE TABLE {DB_LIST} (
                    id INT PRIMARY KEY,
                    stock INT NOT NULL
                );
            """
        )

        conn.commit()
        import_json_data(cursor=cur)
        conn.commit()
        print("Closing cursor connection...")
        cur.close()

        if conn is not None:
            print("Closing database connection...")
            conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            print("Closing database connection...")
            conn.close()


def create_database():
    connection = None
    exists = False

    try:
        print("Opening database connection to default (postgres)...")
        connection = psycopg2.connect(
            "user='postgres' host='localhost' password='postgres' port='5432'"
        )

        if connection is not None:
            connection.autocommit = True
            cur = connection.cursor()
            cur.execute("SELECT datname FROM pg_database;")
            list_database = cur.fetchall()
            database_name = DB_DATABASE

            if (database_name,) not in list_database:
                print("Database does not exist..."
                      f" Creating new database with name: {DB_DATABASE}")
                cur.execute(f'CREATE DATABASE {DB_DATABASE}')
            else:
                print("Database exists!")
                exists = True

            print("Closing cursor connection...")
            cur.close()
            print("Closing database connection...")
            connection.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            print("Closing database connection...")
            connection.close()

    return exists


if __name__ != "__main__":
    print("This file is meant to be run alone to generate the required "
          "database and tables!")
    exit(1)
else:
    if not create_database():
        create_tables()
