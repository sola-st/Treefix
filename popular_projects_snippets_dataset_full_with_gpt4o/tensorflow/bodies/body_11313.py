# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_test_util.py
# This operator is square, so rhs and x will have same shape.
# adjoint value makes no difference because the operator shape doesn't
# change since it is square, but be pedantic.
exit(self.make_x(operator, adjoint=not adjoint, with_batch=with_batch))
