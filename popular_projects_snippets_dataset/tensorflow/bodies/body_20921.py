# Extracted from ./data/repos/tensorflow/tensorflow/python/training/proximal_gradient_descent.py
"""Construct a new proximal gradient descent optimizer.

    Args:
      learning_rate: A Tensor or a floating point value.  The learning
        rate to use.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If True use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "GradientDescent".
    """
super(ProximalGradientDescentOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._l1_regularization_strength = l1_regularization_strength
self._l2_regularization_strength = l2_regularization_strength
self._l1_regularization_strength_tensor = None
self._l2_regularization_strength_tensor = None
