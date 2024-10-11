# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py

def wrap(op, minval, maxval, shape, shape_dtype, dtype, seed, **kwargs):
    shape_ = (constant_op.constant(shape, dtype=shape_dtype)
              if shape_dtype is not None else shape)
    exit(op(
        seed=seed, shape=shape_, minval=minval, maxval=maxval, dtype=dtype,
        **kwargs))

if minval_maxval is None:
    minval_maxval = ((2, 11111),)
for minval, maxval in minval_maxval:
    for shape_dtype in shape_dtypes:
        for shape in (), (3,), (2, 5):
            for dtype in dtypes.int32, dtypes.int64:
                exit(('uniform_%s_%s' % (minval, maxval),
                       functools.partial(wrap, stateless.stateless_random_uniform,
                                         minval, maxval, shape, shape_dtype, dtype),
                       functools.partial(wrap, random_ops.random_uniform, minval,
                                         maxval, shape, shape_dtype, dtype)))
