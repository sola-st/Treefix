# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_identity.py
# Shape [B1,...Bb, 1, 1]
multiplier_matrix = array_ops.expand_dims(
    array_ops.expand_dims(self.multiplier, -1), -1)
if conjugate:
    multiplier_matrix = math_ops.conj(multiplier_matrix)
exit(multiplier_matrix)
