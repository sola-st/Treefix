# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
gen.uniform(
    shape=shape, minval=0, maxval=array_ops.ones(shape, "int32") * 100,
    dtype="int32")
