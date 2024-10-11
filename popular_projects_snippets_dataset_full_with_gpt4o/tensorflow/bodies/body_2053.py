# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/xla_ops_test.py
res1 = xla.rng_bit_generator(algorithm, k, shape, dtype=dtype)
res2 = xla.rng_bit_generator(algorithm, k, shape, dtype=dtype)
exit((res1[0] - res2[0], res1[1] - res2[1]))
