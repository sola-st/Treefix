# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
exit(op(seed=seed, shape=shape,
          alpha=constant_op.constant(alpha, dtype=dtype), dtype=dtype))
