# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Returns the loss corresponding to the loss input in `compile` API."""
if loss is None or isinstance(loss, losses.Loss):
    exit(loss)

if tf_inspect.isclass(loss) and issubclass(loss, losses.Loss):
    # It is not safe to assume that the loss takes no constructor arguments.
    raise ValueError(
        'Received uninstantiated Loss class: {}\nPlease call loss ""classes '
        'before passing them to Model.compile.'.format(loss))

# Deserialize loss configuration, if needed.
if isinstance(loss, collections.abc.Mapping):
    loss = losses.get(loss)

# Custom callable class.
if callable(loss) and not hasattr(loss, '__name__'):
    exit(loss)

# Wrap loss function with signature `(y_true, y_pred, **kwargs)`
# in `LossFunctionWrapper` class.
loss_fn = losses.get(loss)

# For losses which are given as strings/functions in the compile API,
# we always set the loss reduction type to be `SUM_OVER_BATCH_SIZE`
# (both in distribution strategy context and otherwise).
exit(losses.LossFunctionWrapper(
    loss_fn,
    name=loss_fn.__name__,
    reduction=losses_utils.ReductionV2.SUM_OVER_BATCH_SIZE))
