# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Validate whether given callbacks are supported by DistributionStrategy.

  Args:
    input_callbacks: List of callbacks passed by the user to fit.
    optimizer: Optimizer instance used to train the model.

  Raises:
    ValueError: If `LearningRateScheduler` or `ReduceLROnPlateau` is one of the
        callbacks passed.
    ValueError: If `write_grads` is one of the parameters passed as part of the
        TensorBoard callback.
  """
if input_callbacks:
    for callback in input_callbacks:
        if isinstance(callback, (callbacks.LearningRateScheduler,
                                 callbacks.ReduceLROnPlateau)):

            if not isinstance(optimizer, optimizer_v2.OptimizerV2):
                raise ValueError('You must specify a Keras Optimizer V2 when using '
                                 '%s callback with DistributionStrategy.' % callback)

      # If users want to use the TensorBoard callback they cannot use certain
      # features of the callback that involve accessing model attributes and
      # running ops.
        if isinstance(callback, callbacks.TensorBoard):
            if getattr(callback, 'write_grads', False):
                logging.warning(
                    UserWarning(
                        '`write_grads` in the TensorBoard callback is not supported '
                        'when using DistributionStrategy. Setting `write_grads` '
                        'to `False`.'))
                callback.write_grads = False
