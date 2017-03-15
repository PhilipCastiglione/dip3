import sys
import psycopg2
import random

db_name = 'schema-test'
db_host = 'localhost'
db_user = 'philipcastiglione'

def build(cursor):
    cursor.execute("CREATE SCHEMA north;")
    cursor.execute("CREATE SCHEMA south;")
    cursor.execute("CREATE TABLE north.products (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, price INTEGER, in_stock BOOLEAN DEFAULT true);")
    cursor.execute("CREATE TABLE south.products (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, price INTEGER, in_stock BOOLEAN DEFAULT true);")
    cursor.execute("INSERT INTO north.products (name, price, in_stock) VALUES ('widget', 100, true), ('wodget', 50, true), ('gadget', 200, false);")
    cursor.execute("INSERT INTO south.products (name, price, in_stock) VALUES ('foo', 30, true), ('bar', 15, true), ('baz', 20, false);")

def drop(cursor):
    cursor.execute("DROP SCHEMA north CASCADE;")
    cursor.execute("DROP SCHEMA south CASCADE;")

def select(cursor):
    cursor.execute("SELECT * FROM north.products;")
    print("north products")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM south.products;")
    print("south products")
    print(cursor.fetchall())

def record_count(cursor, schema):
    cursor.execute("SELECT COUNT(*) FROM {}.products;".format(schema))
    return cursor.fetchone()

def add(cursor, schema):
    name = "prod" + str(record_count(cursor, schema)[0])
    price = random.randint(1, 200)
    cursor.execute("INSERT INTO {}.products (name, price) VALUES ('{}', {});".format(schema, name, price))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("provide a command, yo")

    connection =  psycopg2.connect(dbname=db_name, host=db_host, user=db_user)
    with connection.cursor() as cursor:
        command = sys.argv[1]
        if command == 'build':
            build(cursor)
        elif command == 'drop':
            drop(cursor)
        elif command == 'select':
            select(cursor)
        elif command == 'add':
            if random.randint(0, 1) < 1:
                add(cursor, 'north')
            else:
                add(cursor, 'south')
        else:
            exit("provide a command I actually know pls")

    connection.commit()
    connection.close()
