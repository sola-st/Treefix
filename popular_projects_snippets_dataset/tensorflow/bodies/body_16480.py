# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_ops.py
"""Computes dropout.

  For each element of `x`, with probability `rate`, outputs `0`, and otherwise
  scales up the input by `1 / (1-rate)`. The scaling is such that the expected
  sum is unchanged.

  By default, each element is kept or dropped independently.  If `noise_shape`
  is specified, it must be
  [broadcastable](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
  to the shape of `x`, and only dimensions with `noise_shape[i] == shape(x)[i]`
  will make independent decisions.  For example, if `shape(x) = [k, l, m, n]`
  and `noise_shape = [k, 1, 1, n]`, each batch and channel component will be
  kept independently and each row and column will be kept or not kept together.

  Args:
    x: A floating point tensor.
    keep_prob: (deprecated) A deprecated alias for `(1-rate)`.
    noise_shape: A 1-D integer `Tensor`, representing the
      shape for randomly generated keep/drop flags.
    seed: A Python integer. Used to create random seeds. See
      `tf.random.set_seed` for behavior.
    name: A name for this operation (optional).
    rate: A scalar `Tensor` with the same type as `x`. The probability that each
      element of `x` is discarded.

  Returns:
    A Tensor of the same shape of `x`.

  Raises:
    ValueError: If `rate` is not in `[0, 1)` or if `x` is not a floating
      point tensor.
  """
try:
    rate_from_keep_prob = 1. - keep_prob if keep_prob is not None else None
except TypeError:
    raise ValueError("`keep_prob` must be a floating point number or Tensor. "
                     f"Received: keep_prob={keep_prob}")

rate = deprecation.deprecated_argument_lookup(
    "rate", rate,
    "keep_prob", rate_from_keep_prob)

if rate is None:
    raise ValueError(f"`rate` must be provided. Received: rate={rate}")

exit(dropout_v2(x, rate, noise_shape=noise_shape, seed=seed, name=name))
