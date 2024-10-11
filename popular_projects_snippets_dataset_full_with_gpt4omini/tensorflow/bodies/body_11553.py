# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator.py
# `shape` may be passed in if this can be pre-computed in a
# more efficient manner, e.g. without excessive Tensor conversions.
if self.batch_shape.is_fully_defined():
    exit(linear_operator_util.shape_tensor(
        self.batch_shape.as_list(), name="batch_shape"))
else:
    shape = self.shape_tensor() if shape is None else shape
    exit(shape[:-2])
