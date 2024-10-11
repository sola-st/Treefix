# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
"""Tests that proper errors are raised.
    """
shape = [2, 3]
with self.assertRaisesWithPredicateMatch(
    ValueError,
    'minval must be a scalar; got a tensor of shape '):
    @def_function.function
    def f():
        stateless.stateless_random_uniform(
            shape=shape, seed=[1, 2], minval=array_ops.zeros(shape, 'int32'),
            maxval=100, dtype='int32')
    f()
with self.assertRaisesWithPredicateMatch(
    ValueError,
    'maxval must be a scalar; got a tensor of shape '):
    @def_function.function
    def f2():
        stateless.stateless_random_uniform(
            shape=shape, seed=[1, 2], minval=0,
            maxval=array_ops.ones(shape, 'int32') * 100,
            dtype='int32')
    f2()
