# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/remote_memory_test.py
with ops.device("job:worker/replica:0/task:0/device:CPU:0"):
    x = array_ops.zeros([1000, 1000], dtypes.int32)

local_func(x)
