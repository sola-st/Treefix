# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
if coord:
    coord.register_thread(threading.current_thread())
time.sleep(n_secs)
