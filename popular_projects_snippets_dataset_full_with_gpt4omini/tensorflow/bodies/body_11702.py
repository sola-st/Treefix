# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
"""Set attributes self._diag_update and self._diag_operator."""
if diag_update is not None:
    self._diag_operator = linear_operator_diag.LinearOperatorDiag(
        self._diag_update, is_positive_definite=is_diag_update_positive)
else:
    if tensor_shape.dimension_value(self.u.shape[-1]) is not None:
        r = tensor_shape.dimension_value(self.u.shape[-1])
    else:
        r = array_ops.shape(self.u)[-1]
    self._diag_operator = linear_operator_identity.LinearOperatorIdentity(
        num_rows=r, dtype=self.dtype)
