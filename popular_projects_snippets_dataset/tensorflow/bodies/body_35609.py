# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
stateless.stateless_random_uniform(
    shape=shape, seed=[1, 2], minval=0,
    maxval=array_ops.ones(shape, 'int32') * 100,
    dtype='int32')
