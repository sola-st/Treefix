# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
"""Standard deviation.

    Standard deviation is defined as,

    ```none
    stddev = E[(X - E[X])**2]**0.5
    ```

    where `X` is the random variable associated with this distribution, `E`
    denotes expectation, and `stddev.shape = batch_shape + event_shape`.

    Args:
      name: Python `str` prepended to names of ops created by this function.

    Returns:
      stddev: Floating-point `Tensor` with shape identical to
        `batch_shape + event_shape`, i.e., the same shape as `self.mean()`.
    """

with self._name_scope(name):
    try:
        exit(self._stddev())
    except NotImplementedError as original_exception:
        try:
            exit(math_ops.sqrt(self._variance()))
        except NotImplementedError:
            raise original_exception
