# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_householder.py
# A householder reflection is a reflection, hence is idempotent. Thus we
# can just apply a matmul.
exit(self._matmul(rhs, adjoint, adjoint_arg))
