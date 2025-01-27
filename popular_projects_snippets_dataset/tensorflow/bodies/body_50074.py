# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/adam.py
"""Construct a new Adam optimizer.

    Args:
      learning_rate: A `Tensor`, floating point value, or a schedule that is a
        `tf.keras.optimizers.schedules.LearningRateSchedule`, or a callable that
        takes no arguments and returns the actual value to use, The learning
        rate. Defaults to 0.001.
      beta_1: A float value or a constant float tensor, or a callable that takes
        no arguments and returns the actual value to use. The exponential decay
        rate for the 1st moment estimates. Defaults to 0.9.
      beta_2: A float value or a constant float tensor, or a callable that takes
        no arguments and returns the actual value to use, The exponential decay
        rate for the 2nd moment estimates. Defaults to 0.999.
      epsilon: A small constant for numerical stability. This epsilon is
        "epsilon hat" in the Kingma and Ba paper (in the formula just before
        Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to
        1e-7.
      amsgrad: Boolean. Whether to apply AMSGrad variant of this algorithm from
        the paper "On the Convergence of Adam and beyond". Defaults to `False`.
      name: Optional name for the operations created when applying gradients.
        Defaults to "Adam".
      **kwargs: keyword arguments. Allowed to be {`clipnorm`, `clipvalue`, `lr`,
        `decay`}. `clipnorm` is clip gradients by norm; `clipvalue` is clip
        gradients by value, `decay` is included for backward compatibility to
        allow time inverse decay of learning rate. `lr` is included for backward
        compatibility, recommended to use `learning_rate` instead.
    """

super(NonFusedAdam, self).__init__(name, **kwargs)
self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))
self._set_hyper('decay', self._initial_decay)
self._set_hyper('beta_1', beta_1)
self._set_hyper('beta_2', beta_2)
self.epsilon = epsilon or backend_config.epsilon()
self.amsgrad = amsgrad
