# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_adjoint.py
# Rotate last dimension
shape = self.operator.shape
exit(shape[:-2].concatenate([shape[-1], shape[-2]]))
