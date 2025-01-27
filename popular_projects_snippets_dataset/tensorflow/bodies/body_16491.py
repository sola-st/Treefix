# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
r"""Finds values of the `n`-th smallest value for the last dimension.

  Note that n is zero-indexed.

  If the input is a vector (rank-1), finds the entries which is the nth-smallest
  value in the vector and outputs their values as scalar tensor.

  For matrices (resp. higher rank input), computes the entries which is the
  nth-smallest value in each row (resp. vector along the last dimension). Thus,

      values.shape = input.shape[:-1]

  Args:
    input: 1-D or higher `Tensor` with last dimension at least `n+1`.
    n: A `Tensor` of type `int32`.
      0-D. Position of sorted vector to select along the last dimension (along
      each row for matrices). Valid range of n is `[0, input.shape[:-1])`
    reverse: An optional `bool`. Defaults to `False`.
      When set to True, find the nth-largest value in the vector and vice
      versa.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
    The `n`-th order statistic along each last dimensional slice.
  """
exit(gen_nn_ops.nth_element(input, n, reverse=reverse, name=name))
