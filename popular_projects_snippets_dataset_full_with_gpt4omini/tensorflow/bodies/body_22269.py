# Extracted from ./data/repos/tensorflow/tensorflow/python/training/adadelta.py
"""Construct a new Adadelta optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value. The learning rate.
        To match the exact form in the original paper use 1.0.
      rho: A `Tensor` or a floating point value. The decay rate.
      epsilon: A `Tensor` or a floating point value.  A constant epsilon used
               to better conditioning the grad update.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Adadelta".


    """
super(AdadeltaOptimizer, self).__init__(use_locking, name)
self._lr = learning_rate
self._rho = rho
self._epsilon = epsilon

# Tensor versions of the constructor arguments, created in _prepare().
self._lr_t = None
self._rho_t = None
self._epsilon_t = None
