# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
exit(op(seed=seed, shape=shape,
          lam=constant_op.constant(lam_dtype(lam), dtype=lam_dtype),
          dtype=out_dtype))
