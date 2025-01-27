# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
"""Settable attribute indicating whether the model should run eagerly.

    Running eagerly means that your model will be run step by step,
    like Python code. Your model might run slower, but it should become easier
    for you to debug it by stepping into individual layer calls.

    By default, we will attempt to compile your model to a static graph to
    deliver the best execution performance.

    Returns:
      Boolean, whether the model should run eagerly.
    """
if self.dynamic and self._run_eagerly is False:  # pylint:disable=g-bool-id-comparison
    # TODO(fchollet): consider using py_func to enable this.
    raise ValueError('Your model contains layers that can only be '
                     'successfully run in eager execution (layers '
                     'constructed with `dynamic=True`). '
                     'You cannot set `run_eagerly=False`.')

if self._cluster_coordinator and self._run_eagerly:
    raise ValueError('When using `Model` with `ParameterServerStrategy`, '
                     '`run_eagerly` is not supported.')

# Run eagerly logic, by priority:
# (1) Dynamic models must be run eagerly.
# (2) Explicitly setting run_eagerly causes a Model to be run eagerly.
# (3) Not explicitly setting run_eagerly defaults to TF's global setting.
exit((self.dynamic or self._run_eagerly or
        (def_function.functions_run_eagerly() and
         self._run_eagerly is None)))
