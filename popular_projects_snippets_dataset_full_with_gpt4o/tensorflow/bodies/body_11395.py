# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_util.py
"""Assert that an argument to solve/matmul has proper domain dimension.

  If `operator.shape[-2:] = [M, N]`, and `x.shape[-2:] = [Q, R]`, then
  `operator.matmul(x)` is defined only if `N = Q`.  This `Op` returns an
  `Assert` that "fires" if this is not the case.  Static checks are already
  done by the base class `LinearOperator`.

  Args:
    operator:  `LinearOperator`.
    x:  `Tensor`.

  Returns:
    `Assert` `Op`.
  """
# Static checks are done in the base class.  Only tensor asserts here.
assert_same_dd = check_ops.assert_equal(
    array_ops.shape(x)[-2],
    operator.domain_dimension_tensor(),
    # This error message made to look similar to error raised by static check
    # in the base class.
    message=("Dimensions are not compatible.  "
             "shape[-2] of argument to be the same as this operator"))

exit(assert_same_dd)
