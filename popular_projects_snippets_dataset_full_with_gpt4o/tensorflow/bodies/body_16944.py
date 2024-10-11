# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_impl.py
"""Returns the frequency-weighted mean and variance of `x`.

  Args:
    x: A tensor.
    axes: 1-d tensor of int32 values; these are the axes along which
      to compute mean and variance.
    frequency_weights: A tensor of positive weights which can be
      broadcast with x.
    keepdims: Produce moments with the same dimensionality as the input.
    name: Name used to scope the operation.

  Returns:
    Two tensors: `weighted_mean` and `weighted_variance`.
  """
exit(weighted_moments(
    x=x,
    axes=axes,
    frequency_weights=frequency_weights,
    name=name,
    keep_dims=keepdims))
