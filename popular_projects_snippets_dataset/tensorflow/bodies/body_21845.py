# Extracted from ./data/repos/tensorflow/tensorflow/python/training/ftrl.py
r"""Construct a new FTRL optimizer.

    Args:
      learning_rate: A float value or a constant float `Tensor`.
      learning_rate_power: A float value, must be less or equal to zero.
        Controls how the learning rate decreases during training. Use zero for
        a fixed learning rate. See section 3.1 in (McMahan et al., 2013).
      initial_accumulator_value: The starting value for accumulators.
        Only zero or positive values are allowed.
      l1_regularization_strength: A float value, must be greater than or
        equal to zero.
      l2_regularization_strength: A float value, must be greater than or
        equal to zero.
      use_locking: If `True` use locks for update operations.
      name: Optional name prefix for the operations created when applying
        gradients.  Defaults to "Ftrl".
      accum_name: The suffix for the variable that keeps the gradient squared
        accumulator.  If not present, defaults to name.
      linear_name: The suffix for the variable that keeps the linear gradient
        accumulator.  If not present, defaults to name + "_1".
      l2_shrinkage_regularization_strength: A float value, must be greater than
        or equal to zero. This differs from L2 above in that the L2 above is a
        stabilization penalty, whereas this L2 shrinkage is a magnitude penalty.
        The FTRL formulation can be written as:
        w_{t+1} = argmin_w(\hat{g}_{1:t}w + L1*||w||_1 + L2*||w||_2^2), where
        \hat{g} = g + (2*L2_shrinkage*w), and g is the gradient of the loss
        function w.r.t. the weights w.
        Specifically, in the absence of L1 regularization, it is equivalent to
        the following update rule:
        w_{t+1} = w_t - lr_t / (beta + 2*L2*lr_t) * g_t -
                  2*L2_shrinkage*lr_t / (beta + 2*L2*lr_t) * w_t
        where lr_t is the learning rate at t.
        When input is sparse shrinkage will only happen on the active weights.
      beta: A float value; corresponds to the beta parameter in the paper.

    Raises:
      ValueError: If one of the arguments is invalid.

    References:
      Ad-click prediction:
        [McMahan et al., 2013](https://dl.acm.org/citation.cfm?id=2488200)
        ([pdf](https://dl.acm.org/ft_gateway.cfm?id=2488200&ftid=1388399&dwn=1&CFID=32233078&CFTOKEN=d60fe57a294c056a-CB75C374-F915-E7A6-1573FBBC7BF7D526))
    """
super(FtrlOptimizer, self).__init__(use_locking, name)

if initial_accumulator_value < 0.0:
    raise ValueError(
        "initial_accumulator_value %f needs to be positive or zero" %
        initial_accumulator_value)
if learning_rate_power > 0.0:
    raise ValueError("learning_rate_power %f needs to be negative or zero" %
                     learning_rate_power)
if l1_regularization_strength < 0.0:
    raise ValueError(
        "l1_regularization_strength %f needs to be positive or zero" %
        l1_regularization_strength)
if l2_regularization_strength < 0.0:
    raise ValueError(
        "l2_regularization_strength %f needs to be positive or zero" %
        l2_regularization_strength)
if l2_shrinkage_regularization_strength < 0.0:
    raise ValueError(
        "l2_shrinkage_regularization_strength %f needs to be positive"
        " or zero" % l2_shrinkage_regularization_strength)

self._learning_rate = learning_rate
self._learning_rate_power = learning_rate_power
self._initial_accumulator_value = initial_accumulator_value
self._l1_regularization_strength = l1_regularization_strength
self._l2_regularization_strength = l2_regularization_strength
self._beta = (0.0 if beta is None else beta)
self._l2_shrinkage_regularization_strength = (
    l2_shrinkage_regularization_strength)
self._learning_rate_tensor = None
self._learning_rate_power_tensor = None
self._l1_regularization_strength_tensor = None
self._adjusted_l2_regularization_strength_tensor = None
self._l2_shrinkage_regularization_strength_tensor = None
self._accum_name = accum_name
self._linear_name = linear_name
