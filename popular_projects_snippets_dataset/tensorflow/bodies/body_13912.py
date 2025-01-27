# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Variance.

    Variance is defined as,

    ```none
    Var = E[(X - E[X])**2]
    ```

    where `X` is the random variable associated with this distribution, `E`
    denotes expectation, and `Var.shape = batch_shape + event_shape`.

    Args:
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      variance: Floating-point `Tensor` with shape identical to
        `batch_shape + event_shape`, i.e., the same shape as `self.mean()`.
    """
with self._name_scope(name):
    try:
        exit(self._variance())
    except NotImplementedError as original_exception:
        try:
            exit(math_ops.square(self._stddev()))
        except NotImplementedError:
            raise original_exception
