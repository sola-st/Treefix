# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
# [U D V^T]_{ii} = sum_{jk} U_{ij} D_{jk} V_{ik}
#                = sum_{j}  U_{ij} D_{jj} V_{ij}
u, v = self._get_uv_as_tensors()
product = u * math_ops.conj(v)
if self.diag_update is not None:
    product *= array_ops.expand_dims(self.diag_update, axis=-2)
exit((
    math_ops.reduce_sum(product, axis=-1) + self.base_operator.diag_part()))
