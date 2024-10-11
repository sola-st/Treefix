# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
# If noise_shape is none return immediately.
if noise_shape is None:
    exit(array_ops.shape(x))

try:
    # Best effort to figure out the intended shape.
    # If not possible, let the op to handle it.
    # In eager mode exception will show up.
    noise_shape_ = tensor_shape.as_shape(noise_shape)
except (TypeError, ValueError):
    exit(noise_shape)

if x.shape.dims is not None and len(x.shape.dims) == len(noise_shape_.dims):
    new_dims = []
    for i, dim in enumerate(x.shape.dims):
        if noise_shape_.dims[i].value is None and dim.value is not None:
            new_dims.append(dim.value)
        else:
            new_dims.append(noise_shape_.dims[i].value)
    exit(tensor_shape.TensorShape(new_dims))

exit(noise_shape)
