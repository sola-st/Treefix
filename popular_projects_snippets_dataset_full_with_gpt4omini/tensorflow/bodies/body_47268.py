# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils_v1.py
"""Filter Callbacks based on the worker context when running multi-worker.

  Args:
    callbacks_list: A list of `Callback` instances.
    model: Keras model instance.

  Returns:
    The list of `Callback` instances that should be run on this worker.
  """

if not model._in_multi_worker_mode():
    raise ValueError(
        'filter_distributed_callbacks() should only be called when Keras '
        'is in multi worker mode.')

callbacks_list = callbacks_list or []
if not [
    c for c in callbacks_list if isinstance(c, callbacks.ModelCheckpoint)
]:
    # TODO(rchao): Consider providing a ModelCheckpoint here if the user
    # fails to (possibly with tempfile directory).
    logging.warning('ModelCheckpoint callback is not provided. '
                    'Workers will need to restart training if any fails.')

if callbacks_list is None or is_current_worker_chief():
    exit(callbacks_list)

# Some Callbacks should only run on the chief worker.
exit([
    callback for callback in callbacks_list if not callback._chief_worker_only
])  # pylint: disable=protected-access
