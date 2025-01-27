# Extracted from ./data/repos/tensorflow/tensorflow/python/training/momentum.py
"""Construct a new Momentum optimizer.

    Args:
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
      momentum: A `Tensor` or a floating point value.  The momentum.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Momentum".
      use_nesterov: If `True` use Nesterov Momentum.
        See (Sutskever et al., 2013).
        This implementation always computes gradients at the value of the
        variable(s) passed to the optimizer. Using Nesterov Momentum makes the
        variable(s) track the values called `theta_t + mu*v_t` in the paper.
        This implementation is an approximation of the original formula, valid
        for high values of momentum. It will compute the "adjusted gradient"
        in NAG by assuming that the new gradient will be estimated by the
        current average gradient plus the product of momentum and the change
        in the average gradient.

    References:
      On the importance of initialization and momentum in deep learning:
        [Sutskever et al., 2013]
        (http://proceedings.mlr.press/v28/sutskever13.html)
        ([pdf](http://proceedings.mlr.press/v28/sutskever13.pdf))


    """
super(MomentumOptimizer, self).__init__(use_locking, name)
self._learning_rate = learning_rate
self._momentum = momentum
self._use_nesterov = use_nesterov
