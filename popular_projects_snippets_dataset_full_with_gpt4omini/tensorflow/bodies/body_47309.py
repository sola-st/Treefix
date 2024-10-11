# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distributed_training_utils.py
"""Call a function that uses replica-local variables.

  This function correctly handles calling `fn` in a cross-replica
  context.

  Args:
    fn: The function to call.
    *args: Positional arguments to the `fn`.
    **kwargs: Keyword argument to `fn`.

  Returns:
    The result of calling `fn`.
  """
# TODO(b/132666209): Remove this function when we support assign_*
# for replica-local variables.
strategy = None
if 'strategy' in kwargs:
    strategy = kwargs.pop('strategy')
else:
    if ds_context.has_strategy():
        strategy = ds_context.get_strategy()

  # TODO(b/120571621): TPUStrategy does not implement replica-local variables.
is_tpu = backend.is_tpu_strategy(strategy)
if ((not is_tpu) and strategy and ds_context.in_cross_replica_context()):
    with strategy.scope():
        exit(strategy.extended.call_for_each_replica(fn, args, kwargs))
exit(fn(*args, **kwargs))
