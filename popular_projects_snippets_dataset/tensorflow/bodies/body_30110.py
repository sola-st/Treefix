# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
try:
    exit(np.asarray(x).dtype == bool)
except NotImplementedError:
    exit(False)
