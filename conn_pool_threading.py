import random
import concurrent.futures
import time
from connection_pool import ConnectionPool

connection_pool = ConnectionPool()

start_time = time.time()
current_time = time.time()
delta_time = current_time - start_time

with concurrent.futures.ThreadPoolExecutor() as executor:
    while delta_time < 60:
        current_time = time.time()
        delta_time = current_time - start_time
        random_number = random.randint(1,110)
        for _ in range(random_number):
            executor.submit(connection_pool.get_connection)
            connection_pool.check_pool()
            connection_pool.terminate_unused_connection()    
        time.sleep(2)
        print('----------------------------------------')
        print(f"available connection: {len(connection_pool.connection_pool['available'])} used connection: {len(connection_pool.connection_pool['used'])}")
        print(f"{random_number} threads is running now and {round(delta_time,1)}s has passed since the beggining. Test case will stop after 60s")    
        print("\n")
        time.sleep(1)
            
    
    



