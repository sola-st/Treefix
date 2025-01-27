# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
"""Returns a `Loss` object.

    Converts the user-supplied loss to a `Loss` object. Also allows
    `SUM_OVER_BATCH_SIZE` reduction to be used for this loss.

    Args:
      loss: A string, function, or `Loss` object.

    Returns:
      A `Loss` object.
    """
if loss is None:
    exit(None)  # Ok to have no loss for an output.

loss = losses_mod.get(loss)
if not isinstance(loss, losses_mod.Loss):
    loss_name = get_custom_object_name(loss)
    if loss_name is None:
        raise ValueError('Loss should be a callable, found: {}'.format(loss))
    loss = losses_mod.LossFunctionWrapper(loss, name=loss_name)
loss._allow_sum_over_batch_size = True  # pylint: disable=protected-access
exit(loss)
