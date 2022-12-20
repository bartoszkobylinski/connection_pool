import random
import threading
import concurrent.futures
import time
from connection_pool import ConnectionPool, DBConnection
from random import randint

connection_pool = ConnectionPool()

start_time = time.time()
current_time = time.time()
delta_time = current_time - start_time

with concurrent.futures.ThreadPoolExecutor() as executor:
    while delta_time < 60:
        current_time = time.time()
        delta_time = current_time - start_time
        #executor.submit(counting)
        #print(f"I'm before loop and counter is: {counter} ")
        random_number = random.randint(1,150)
        for _ in range(random_number):
            executor.submit(connection_pool.get_connection)
            connection_pool.check_pool()
            connection_pool.terminate_unused_connection()    
        time.sleep(1)
        print(f"available connection: {len(connection_pool.connection_pool['available'])} used connection: {len(connection_pool.connection_pool['used'])}")
        print(f"{random_number} threads is running now and {delta_time}s has passed since the beggining. Procees will stop after 60s")    
        print("\n")
            
    
    



