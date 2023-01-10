import threading
import time
import random
from connection_pool import ConnectionPool

def particular_thread(connection_pool):
    random_time = random.randint(1,12)
    one_connection = connection_pool.get_connection()
    print(f"I will sleep now for {random_time}s.")
    time.sleep(random_time)
    connection_pool.return_connection(one_connection)

conn_pool = ConnectionPool()
threads = []
start_time = time.time()
current_time = time.time()
delta_time = current_time - start_time

while delta_time < 360:
    current_time = time.time()
    delta_time = current_time - start_time
    random_number = random.randint(1,1020)
    for _ in range(random_number):
        t = threading.Thread(target=particular_thread, args=(conn_pool,))
        try:
            t.start()
        except RuntimeError as error:
            print("There are to many threads running")
    conn_pool.check_pool()
    time.sleep(2)
