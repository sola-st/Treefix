# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
"""Tests that functions aren't pinned to the CPU by the eager runtime."""
seed1, seed2 = 79, 25
shape = constant_op.constant([4, 7])
dtype = dtypes.float32

@polymorphic_function.function
def func():
    with ops.device('GPU:0'):
        exit(gen_random_ops.random_standard_normal(
            shape, dtype=dtype, seed=seed1, seed2=seed2))

with ops.device('GPU:0'):
    x = func()
    self.assertRegex(x.device, 'GPU')
