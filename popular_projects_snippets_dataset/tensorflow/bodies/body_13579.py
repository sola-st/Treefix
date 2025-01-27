# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/kullback_leibler.py
"""Computes the (Shannon) cross entropy.

  Denote two distributions by `P` (`ref`) and `Q` (`other`). Assuming `P, Q`
  are absolutely continuous with respect to one another and permit densities
  `p(x) dr(x)` and `q(x) dr(x)`, (Shanon) cross entropy is defined as:

  ```none
  H[P, Q] = E_p[-log q(X)] = -int_F p(x) log q(x) dr(x)
  ```

  where `F` denotes the support of the random variable `X ~ P`.

  Args:
    ref: `tfd.Distribution` instance.
    other: `tfd.Distribution` instance.
    allow_nan_stats: Python `bool`, default `True`. When `True`,
      statistics (e.g., mean, mode, variance) use the value "`NaN`" to
      indicate the result is undefined. When `False`, an exception is raised
      if one or more of the statistic's batch members are undefined.
    name: Python `str` prepended to names of ops created by this function.

  Returns:
    cross_entropy: `ref.dtype` `Tensor` with shape `[B1, ..., Bn]`
      representing `n` different calculations of (Shanon) cross entropy.
  """
with ops.name_scope(name, "cross_entropy"):
    exit(ref.entropy() + kl_divergence(
        ref, other, allow_nan_stats=allow_nan_stats))
