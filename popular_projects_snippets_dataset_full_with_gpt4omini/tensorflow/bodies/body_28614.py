# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/cache_test.py
dataset = dataset_ops.Dataset.range(10)
initial_state = constant_op.constant(0, dtypes.int64)
scan_func = lambda state, i: (state + i, state + i)
dataset = dataset.scan(
    initial_state=initial_state, scan_func=scan_func).cache()
expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
self.verifyRandomAccess(dataset, expected)
