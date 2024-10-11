# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/random_generator_test.py
t1 = gen.uniform_full_int(shape=shape, dtype=dtype)
t2 = gen.uniform_full_int(shape=shape, dtype=dtype)
t = array_ops.stack([t1, t2])
exit(t)
