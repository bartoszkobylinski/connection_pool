import unittest
import random
import concurrent.futures
import time
from connection_pool import ConnectionPool, DBConnection

'''
class TestConnectionPool(unittest.TestCase):
    
    def setUp(self):
        self.connection_pool = ConnectionPool()
    
    def test_sthring(self):
        self.assertEqual("Connection established with database: bartoszkobylinski at host: 127 on port: {self.port}")
        host='127.0.0.1', port='5432', database='bartoszkobylinski'
    pass
'''

conn_pool = ConnectionPool()

start_time = time.time()
current_time = time.time()
delta_time = current_time - start_time

counter = list()

def particular_thread(connection_pool):
    a = random.randint(1,1800)
    global counter
    counter.append(a)
    #print(f"I have added element: {a} to counter: {counter} ")
    time.sleep(1.5)
    random_time = random.randint(1,12)
    one_connection = connection_pool.get_connection()
    print(f"I will sleep now for {random_time}s.")
    time.sleep(random_time)
    connection_pool.return_connection(one_connection)



#with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
'''
while delta_time < 60:
    current_time = time.time()
    delta_time = current_time - start_time
    random_number = random.randint(1,381)
    with concurrent.futures.ThreadPoolExecutor(max_workers=random_number) as executor:
        executor.submit(particular_thread,conn_pool)
        conn_pool.check_pool()   
        print(f"Length of executor thread: {len(executor._threads)} and max_workers is set to: {executor._max_workers} and random number: {random_number}")
        time.sleep(2)
        print('----------------------------------------')
        print(f"available connection: {len(conn_pool.connection_pool['available'])} used connection: {len(conn_pool.connection_pool['used'])}")
        print(f"{random_number} threads is running now and {round(delta_time,1)}s has passed since the beggining. Test case will stop after 60s")    
        print("\n")
    
    print(f"Len of counter : {len(counter)}")
    time.sleep(2)
'''
