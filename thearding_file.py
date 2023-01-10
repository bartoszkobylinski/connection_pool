import threading
import time
import random
from conn_pool_threading import particular_thread
from connection_pool import ConnectionPool

conn_pool = ConnectionPool()




#particular_thread(connection_pool=conn_pool)

threads = []
'''
for _ in range(100):
    t = threading.Thread(target=particular_thread, args=(conn_pool,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
'''
start_time = time.time()
current_time = time.time()
delta_time = current_time - start_time

while delta_time < 360:
    current_time = time.time()
    delta_time = current_time - start_time
    random_number = random.randint(1,11020)
    for _ in range(random_number):
        t = threading.Thread(target=particular_thread, args=(conn_pool,))
        try:
            t.start()
        except RuntimeError as error:
            print("The is to many threads running")
    conn_pool.check_pool()
    time.sleep(2)
