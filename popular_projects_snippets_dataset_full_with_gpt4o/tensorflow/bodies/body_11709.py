# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_low_rank_update.py
# Recall this operator is:
#   A = L + UDV^H.
# So in one case self-adjoint depends only on L
if self.u is self.v and self.diag_update is None:
    exit(self.base_operator.assert_self_adjoint())
# In all other cases, sufficient conditions for self-adjoint can be found
# efficiently. However, those conditions are not necessary conditions.
exit(super(LinearOperatorLowRankUpdate, self).assert_self_adjoint())
