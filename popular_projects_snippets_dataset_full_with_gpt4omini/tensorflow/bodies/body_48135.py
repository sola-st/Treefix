# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_v1.py
"""Settable attribute indicating whether the model should run eagerly.

    Running eagerly means that your model will be run step by step,
    like Python code. Your model might run slower, but it should become easier
    for you to debug it by stepping into individual layer calls.

    By default, we will attempt to compile your model to a static graph to
    deliver the best execution performance.

    Returns:
      Boolean, whether the model should run eagerly.
    """
if self._run_eagerly is True and not context.executing_eagerly():
    raise ValueError('You can only set `run_eagerly=True` if eager execution '
                     'is enabled.')
if not self.dynamic:
    if self._run_eagerly is None:
        # Respect `tf.config.run_functions_eagerly` unless
        # `run_eagerly` was explicitly passed to `compile`.
        exit(def_function.functions_run_eagerly())
    else:
        exit(self._run_eagerly)
else:
    if not context.executing_eagerly():
        raise ValueError('Your model contains layers that can only be '
                         'successfully run in eager execution (layers '
                         'constructed with `dynamic=True`). '
                         'You must enable eager execution with '
                         '`tf.enable_eager_execution()`.')
    if self._run_eagerly is False:
        # TODO(fchollet): consider using py_func to enable this.
        raise ValueError('Your model contains layers that can only be '
                         'successfully run in eager execution (layers '
                         'constructed with `dynamic=True`). '
                         'You cannot set `run_eagerly=False`.')
    exit(context.executing_eagerly())
