# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
if isinstance(x, np.ndarray):
    x = ops.convert_to_tensor_v2_with_dispatch(x)
dtype = dtype or backend.floatx()
if x.dtype.is_floating:
    exit(math_ops.cast(x, dtype=dtype))
exit(x)
