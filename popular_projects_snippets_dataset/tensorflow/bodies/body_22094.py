# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages.py
"""Creates a new ExponentialMovingAverage object.

    The `apply()` method has to be called to create shadow variables.
    Follow-on calls to the `apply()` method will update the moving averages
    in the shadow variables.
    (In TF 1.x graphs `apply()` will return an update op to update
    the moving averages which must be explicitly run).

    The optional `num_updates` parameter allows one to tweak the decay rate
    dynamically. It is typical to pass the count of training steps, usually
    kept in a variable that is incremented at each step, in which case the
    decay rate is lower at the start of training.  This makes moving averages
    move faster.  If passed, the actual decay rate used is:

      `min(decay, (1 + num_updates) / (10 + num_updates))`

    Args:
      decay: A scalar float value, `Tensor`, or `Variable`. The decay parameter.
      num_updates: Optional count of number of updates applied to variables.
      zero_debias: If `True`, zero debias moving-averages that are initialized
        with tensors. (Note: moving averages may not be initialized with
        non-variable tensors when eager execution is enabled).
      name: String. Optional prefix name to use for the name of ops added in
        `apply()`.
    """
self._decay = decay
self._num_updates = num_updates
self._zero_debias = zero_debias
self._name = name
self._averages = {}
