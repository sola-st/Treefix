# Extracted from ./data/repos/tensorflow/tensorflow/python/training/gradient_descent.py
"""Construct a new gradient descent optimizer.

    Args:
      learning_rate: A Tensor or a floating point value.  The learning
        rate to use.
      use_locking: If True use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients. Defaults to "GradientDescent".

    @compatibility(eager)
    When eager execution is enabled, `learning_rate` can be a callable that
    takes no arguments and returns the actual value to use. This can be useful
    for changing these values across different invocations of optimizer
    functions.
    @end_compatibility
    """
super(GradientDescentOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._learning_rate_tensor = None
