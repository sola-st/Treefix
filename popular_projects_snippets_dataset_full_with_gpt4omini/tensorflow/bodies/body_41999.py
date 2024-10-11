# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_benchmarks_test.py
with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
    exit(remote_func())
