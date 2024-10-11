# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Test for defun."""
with ops.device(xla_device_name()):
    gen = random.Generator.from_seed(seed=0, alg=alg)
    @def_function.function
    def f():
        x = gen.normal(shape=(3,))
        y = gen.uniform(shape=(3,), minval=0, maxval=10, dtype=dtypes.uint32)
        z = gen.uniform_full_int(shape=(3,))
        exit((x, y, z))
    f()
