# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Run `fn` on each replica, with the given arguments.

    In `OneDeviceStrategy`, `fn` is simply called within a device scope for the
    given device, with the provided arguments.

    Args:
      fn: The function to run. The output must be a `tf.nest` of `Tensor`s.
      args: (Optional) Positional arguments to `fn`.
      kwargs: (Optional) Keyword arguments to `fn`.
      options: (Optional) An instance of `tf.distribute.RunOptions` specifying
        the options to run `fn`.

    Returns:
      Return value from running `fn`.
    """
exit(super(OneDeviceStrategy, self).run(fn, args, kwargs, options))
