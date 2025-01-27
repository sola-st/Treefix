# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Quantile function. Aka "inverse cdf" or "percent point function".

    Given random variable `X` and `p in [0, 1]`, the `quantile` is:

    ```none
    quantile(p) := x such that P[X <= x] == p
    ```

    Args:
      value: `float` or `double` `Tensor`.
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      quantile: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
        values of type `self.dtype`.
    """
exit(self._call_quantile(value, name))
