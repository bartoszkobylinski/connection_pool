import psycopg2
#import this
import timeit
import time
test_code = '''
try:
    db_connection = psycopg2.connect(user='bartoszkobylinski', host = '127.0.0.1', port = '5432', database = "bartoszkobylinski")
    cursor = db_connection.cursor()
    print("PostgreSQL serever information")
    print(db_connection.get_dsn_parameters(), '\n')
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except(Exception) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (db_connection):
        cursor.close()
        db_connection.close()
        print("PostgreSQL connection is closed")
'''

class ConnectionPool:

    def __init__(self):
        self.connection_pool = []
        pass

    def add_connection(self, connection):
        if len(self.connection_pool)< 100:
            self.connection_pool.append(connection)
        else:
            return "There is to many active connection"
        

class DBConnection:

    def __init__(self, user='bartoszkobylinski', host='127.0.0.1', port='5432', database='bartoszkobylinski'):
        self.user = user
        self.host = host
        self.port = port
        self.database = database
        self._connection = psycopg2.connect(user=self.user, host=self.host, port=self.port, database=self.database)
        self._cursor = self._connection.cursor()
        self.timelife = None
        self.available = None

    @property
    def connection(self):
        return self._connection
    
    @property
    def cursor(self):
        return self._cursor
    
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def commit(self):
        self.connection.commit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __str__(self):
        return f"Connection established with database: {self.database} at host: {self.host} on port: {self.port}"

'''
def connection_to_databes():
    x = range(1000000)
    try:
        db_connection = psycopg2.connect(user='bartoszkobylinski',
        host = '127.0.0.1',
        port = '5432',
        database = 'bartoszkobylinski'
            )   
        t1 = time.time()
        for i in x:
            cursor = db_connection.cursor()
            #print("PostgreSQL serever information")
            #print(db_connection.get_dsn_parameters(), '\n')
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("You are connected to - ", record, "\n")
        print(f"this is time:{time.time() - t1}")
    except(Exception) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if db_connection:
            cursor.close()
            db_connection.close()
            print("PostgreSQL connection is closed")
'''

a = DBConnection()
print(a)
a.close()
del a
try:
    print(a)
except NameError as e:
    print("object doesn't exist!")