# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Log probability density/mass function.

    Args:
      value: `float` or `double` `Tensor`.
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      log_prob: a `Tensor` of shape `sample_shape(x) + self.batch_shape` with
        values of type `self.dtype`.
    """
exit(self._call_log_prob(value, name))
