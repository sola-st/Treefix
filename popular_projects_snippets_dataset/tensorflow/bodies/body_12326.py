# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""If `data` is scalar, then add a dimension; otherwise return as-is."""
if data.shape.ndims is not None:
    if data.shape.ndims == 0:
        exit(stack([data]))
    else:
        exit(data)
else:
    data_shape = shape(data)
    data_ndims = rank(data)
    exit(reshape(data, concat([[1], data_shape], axis=0)[-data_ndims:]))
