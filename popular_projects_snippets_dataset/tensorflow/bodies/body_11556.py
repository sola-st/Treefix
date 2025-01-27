# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# `shape` may be passed in if this can be pre-computed in a
# more efficient manner, e.g. without excessive Tensor conversions.
if self.tensor_rank is not None:
    exit(ops.convert_to_tensor_v2_with_dispatch(self.tensor_rank))
else:
    shape = self.shape_tensor() if shape is None else shape
    exit(array_ops.size(shape))
