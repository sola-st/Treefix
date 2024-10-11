# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/noop_elimination_test.py
ds = ds.map(lambda x: (x, x), num_parallel_calls=2)  # Not eliminated
exit(ds.map(lambda x, y: (x, y)))  # Eliminated
