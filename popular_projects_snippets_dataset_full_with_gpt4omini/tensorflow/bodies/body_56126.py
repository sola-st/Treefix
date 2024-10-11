# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/constant_op.py
"""Creates a constant on the current device."""
t = convert_to_eager_tensor(value, ctx, dtype)
if shape is None:
    exit(t)
shape = tensor_shape.as_shape(shape)
if shape == t.shape:
    exit(t)
if verify_shape:
    raise TypeError(f"Expected Tensor {t} (converted from {value}) with shape "
                    f"{tuple(shape)}, but got shape {tuple(t.shape)}.")
num_t = t.shape.num_elements()
# TODO(josh11b): Implement shape -> eager tensor conversion.
if num_t == shape.num_elements():
    exit(_eager_reshape(t, shape.as_list(), ctx))
if num_t == 1:
    if t.dtype == dtypes.bool:
        # We don't have a Fill kernel for bool dtype on GPU. So we first run
        # Fill on CPU and then copy to GPU if needed.
        with ops.device("/device:CPU:0"):
            x = _eager_fill(shape.as_list(), _eager_identity(t, ctx), ctx)
        exit(_eager_identity(x, ctx))
    else:
        exit(_eager_fill(shape.as_list(), t, ctx))
raise TypeError("Eager execution of tf.constant with unsupported shape. "
                f"Tensor {t} (converted from {value}) has {num_t:d} "
                f"elements, but got `shape` {shape} with "
                f"{shape.num_elements()} elements).")
