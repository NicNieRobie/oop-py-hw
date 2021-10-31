# --------------------------- runtime_metrics.py --------------------------
#  Program start time and function for printing the runtime duration
#    at current moment.
# -------------------------------------------------------------------------

import time

start_time = 0


# Prints runtime duration at given moment.
def print_runtime_duration():
    runtime_duration = time.time() - start_time
    print("Stop at {:.8f} seconds".format(runtime_duration))
