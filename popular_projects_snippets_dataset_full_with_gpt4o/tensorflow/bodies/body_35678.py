# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
minval2 = constant_op.constant(minval, dtype=dtype)
maxval2 = constant_op.constant(maxval, dtype=dtype)
exit(gen_random_ops.random_uniform_int(
    shape, minval=minval2, maxval=maxval2, seed=seed1, seed2=seed2))
