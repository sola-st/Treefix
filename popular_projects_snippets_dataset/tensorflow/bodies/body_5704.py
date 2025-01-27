# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/central_storage_strategy.py
"""Run `fn` on each replica, with the given arguments.

    In `CentralStorageStrategy`, `fn` is  called on each of the compute
    replicas, with the provided "per replica" arguments specific to that device.

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Return value from running `fn`.
    """
exit(super(CentralStorageStrategy, self).run(fn, args, kwargs, options))
