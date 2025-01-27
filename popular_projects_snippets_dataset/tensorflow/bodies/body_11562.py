# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# `shape` may be passed in if this can be pre-computed in a
# more efficient manner, e.g. without excessive Tensor conversions.
dim_value = tensor_shape.dimension_value(self.range_dimension)
if dim_value is not None:
    exit(ops.convert_to_tensor_v2_with_dispatch(dim_value))
else:
    shape = self.shape_tensor() if shape is None else shape
    exit(shape[-2])
