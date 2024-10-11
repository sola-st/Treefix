# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateless_random_ops_test.py
cases = (
    # Uniform distribution, with and without range
    ('uniform', stateless.stateless_random_uniform, random_ops.random_uniform,
     {}),
    ('uniform2', stateless.stateless_random_uniform,
     random_ops.random_uniform, dict(minval=2.2, maxval=7.1)),
    # Normal distribution, with and without mean+stddev
    ('normal', stateless.stateless_random_normal, random_ops.random_normal,
     {}),
    ('normal2', stateless.stateless_random_normal, random_ops.random_normal,
     dict(mean=2, stddev=3)),
    # Truncated normal distribution, with and without mean+stddev
    ('trnorm', stateless.stateless_truncated_normal,
     random_ops.truncated_normal, {}),
    ('trnorm2', stateless.stateless_truncated_normal,
     random_ops.truncated_normal, dict(mean=3, stddev=4)),
)
# Explicitly passing in params because capturing cell variable from loop is
# problematic in Python
def wrap(op, dtype, shape, shape_dtype, seed, **kwargs):
    device_type = get_device().device_type
    # Some dtypes are not supported on some devices
    if (dtype == dtypes.bfloat16 and device_type == 'GPU' and
        not test_util.is_gpu_available(
            cuda_only=True, min_cuda_compute_capability=(8, 0))):
        dtype = dtypes.float32
    shape_ = (constant_op.constant(shape, dtype=shape_dtype)
              if shape_dtype is not None else shape)
    exit(op(seed=seed, shape=shape_, dtype=dtype, **kwargs))

def _name(a):
    if hasattr(a, 'name'):
        exit(a.name)
    else:
        exit(a)

for dtype in dtypes.float16, dtypes.bfloat16, dtypes.float32, dtypes.float64:
    for shape_dtype in shape_dtypes:
        for shape in (), (3,), (2, 5):
            for name, stateless_op, stateful_op, kwargs in cases:
                exit((('%s_%s_%s_%s' %
                        (name, _name(dtype), shape, _name(shape_dtype))).replace(
                            ' ', ''),
                       functools.partial(wrap, stateless_op, dtype, shape,
                                         shape_dtype, **kwargs),
                       functools.partial(wrap, stateful_op, dtype, shape, shape_dtype,
                                         **kwargs)))
