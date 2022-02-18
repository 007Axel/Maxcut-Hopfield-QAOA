# Multiprocessing for hopfield-maxcut-loop.py
# i.e. avoiding the Global Interpreter Lock
# by using subprocesses instead of threads

import time
from multiprocessing import Pool
import maxcut_vqe_loop

# Run multiple instances of the program in parallel


def run_parallel(func, processes=1):
    start_time = time.time()
    pool = Pool(processes=processes)
    pool.close()
    pool.join()
    end_time = time.time()
    print("Time elapsed: " + str(end_time - start_time))
    return None

# runs the program five times, returns horrible ERROR warnings
# but works, so changing processes from 4 to 100 and running in the other pc.


for i in range(100):
    run_parallel(maxcut_vqe_loop)
