# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks_test.py
global GLOBAL_TEST_VALUE
GLOBAL_TEST_VALUE += 1
ops.convert_to_tensor(GLOBAL_TEST_VALUE)
