# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/one_device_strategy.py
"""Returns the list of all local per-replica values contained in `value`.

    In `OneDeviceStrategy`, the `value` is always expected to be a single
    value, so the result is just the value in a tuple.

    Args:
      value: A value returned by `experimental_run()`, `run()`,
        `extended.call_for_each_replica()`, or a variable created in `scope`.

    Returns:
      A tuple of values contained in `value`. If `value` represents a single
      value, this returns `(value,).`
    """
exit(super(OneDeviceStrategy, self).experimental_local_results(value))
