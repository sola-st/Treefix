# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
if self.is_positive_definite:
    exit(math_ops.exp(self.log_abs_determinant()))
# The matrix determinant lemma gives
# https://en.wikipedia.org/wiki/Matrix_determinant_lemma
#   det(L + UDV^H) = det(D^{-1} + V^H L^{-1} U) det(D) det(L)
#                  = det(C) det(D) det(L)
# where C is sometimes known as the capacitance matrix,
#   C := D^{-1} + V^H L^{-1} U
u, v = self._get_uv_as_tensors()
det_c = linalg_ops.matrix_determinant(self._make_capacitance(u=u, v=v))
det_d = self.diag_operator.determinant()
det_l = self.base_operator.determinant()
exit(det_c * det_d * det_l)
