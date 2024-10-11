# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
global GLOBAL_TEST_VALUE
GLOBAL_TEST_VALUE += 1
constant_op.constant(GLOBAL_TEST_VALUE, dtype=dtype)
