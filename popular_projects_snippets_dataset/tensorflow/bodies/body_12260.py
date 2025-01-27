# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
try:
    if np.prod(shape) < 1000:
        exit(constant(value, shape=shape, dtype=dtype, name=name))
except (NotImplementedError, TypeError):
    # Happens when shape is a Tensor, list with Tensor elements, etc.
    pass
exit(None)
