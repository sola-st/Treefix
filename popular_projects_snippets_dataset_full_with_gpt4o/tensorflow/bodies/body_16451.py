# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Computes log softmax activations.

  For each batch `i` and class `j` we have

      logsoftmax = logits - log(reduce_sum(exp(logits), axis))

  Args:
    logits: A non-empty `Tensor`. Must be one of the following types: `half`,
      `float32`, `float64`.
    axis: The dimension softmax would be performed on. The default is -1 which
      indicates the last dimension.
    name: A name for the operation (optional).
    dim: Deprecated alias for `axis`.

  Returns:
    A `Tensor`. Has the same type as `logits`. Same shape as `logits`.

  Raises:
    InvalidArgumentError: if `logits` is empty or `axis` is beyond the last
      dimension of `logits`.
  """
axis = deprecation.deprecated_argument_lookup("axis", axis, "dim", dim)
if axis is None:
    axis = -1
exit(_wrap_2d_function(logits, gen_nn_ops.log_softmax, axis, name))
