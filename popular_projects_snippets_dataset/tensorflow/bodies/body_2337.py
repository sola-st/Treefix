# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""A simple test."""
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=0, alg=alg)
    gen.normal(shape=(3,))
    gen.uniform(shape=(3,), minval=0, maxval=10, dtype=dtypes.uint32)
    gen.uniform_full_int(shape=(3,))
