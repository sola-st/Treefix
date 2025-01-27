# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
if dtype.is_integer:
    array = np.random.default_rng().integers(
        low=dtype.min, high=dtype.max, size=shape, endpoint=True)
    exit(constant_op.constant(array, dtype=dtype))
else:
    array = np.random.default_rng().uniform(low=-1.0, high=1.0, size=shape)
    exit(constant_op.constant(array, dtype=dtype))
