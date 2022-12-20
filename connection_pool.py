import psycopg2
#import this
import timeit
import time
import random


class DBConnection:

    def __init__(self, user='bartoszkobylinski', host='127.0.0.1', port='5432', database='bartoszkobylinski'):
        self.user = user
        self.host = host
        self.port = port
        self.database = database
        self._connection = psycopg2.connect(user=self.user, host=self.host, port=self.port, database=self.database)
        self._cursor = self._connection.cursor()
        self.timelife = None
        self.available = True

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


class ConnectionPool(DBConnection):

    def __init__(self):
        connection = DBConnection()
        self.connection_pool = {'available':[], 'used':[]}
        for _ in range(10):
            self.connection_pool.get('available','').append(connection)
        

    
    def get_connection(self):
        if self.connection_pool.get('available',''):
            connection = self.connection_pool.get('available','').pop()
            self.connection_pool.get('used','').append(connection)
            return connection
        else:
            if self.check_pool():
                message = self.check_pool()
                print(message)
            else:
                connection = DBConnection()
                self.connection_pool.get('used').append(connection)
                #print(f"Connection added! Length used connection is: {len(self.connection_pool['used'])}")
                return connection
        
    
    def check_pool(self):
        if len(self.connection_pool.get('available','')) + len(self.connection_pool.get('used','')) > 98:
            return "There is to many connection in the pool"
        elif len(self.connection_pool.get('available','')) > 30:
            self.terminate_unused_connection()
    
    def terminate_unused_connection(self):
        for used_connection in self.connection_pool['used']:
            if len(self.connection_pool['used']) > 5:
                used_connection = self.connection_pool['used'].pop()
                del used_connection
                #print(f"Length of used is: {len(self.connection_pool['used'])}.")

    def __str__(self) -> str:
        return f"Connection pool has: {self.connection_pool}"
        
'''

conn_pool = ConnectionPool()

for _ in range(40):
    conn_pool.get_connection()

print(f"this is len of available connection: {len(conn_pool.connection_pool['available'])} and this is len of used connection:{len(conn_pool.connection_pool['used'])}")

conn_pool.terminate_unused_connection()
    
    


print(f"this is len of available connection: {len(conn_pool.connection_pool['available'])} and this is len of used connection:{len(conn_pool.connection_pool['used'])}")
'''
