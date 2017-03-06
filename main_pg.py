import psycopg2

def create_table():
    dsn = "dbname='testdb' user='homestead' password='secret' host='localhost' port='5432'"
    conn = psycopg2.connect(dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    dsn = "dbname='testdb' user='homestead' password='secret' host='localhost' port='5432'"
    conn = psycopg2.connect(dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()

def view():
    dsn = "dbname='testdb' user='homestead' password='secret' host='localhost' port='5432'"
    conn = psycopg2.connect(dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(item):
    dsn = "dbname='testdb' user='homestead' password='secret' host='localhost' port='5432'"
    conn = psycopg2.connect(dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update(item, quantity, price):
    dsn = "dbname='testdb' user='homestead' password='secret' host='localhost' port='5432'"
    conn = psycopg2.connect(dsn=dsn)
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()

create_table()
#insert("Apple", 10, 15)
#insert("Orange", 10, 15)
#insert("Water Glass", 10, 5)
#delete("Water Glass")
#update("Water Glass", 12, 6)
print(view())
