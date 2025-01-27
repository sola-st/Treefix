# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator_test.py
while True:
    with coord._lock:
        if len(coord._registered_threads) == num_threads:
            break
    time.sleep(0.001)
