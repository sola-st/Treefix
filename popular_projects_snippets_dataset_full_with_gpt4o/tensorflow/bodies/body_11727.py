# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
# Rotate last dimension
shape = self.operator.shape_tensor()
exit(array_ops.concat([
    shape[:-2], [shape[-1], shape[-2]]], axis=-1))
