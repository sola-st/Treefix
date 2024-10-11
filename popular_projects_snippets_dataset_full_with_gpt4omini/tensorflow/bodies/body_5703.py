# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/central_storage_strategy.py
"""Returns the list of all local per-replica values contained in `value`.

    In `CentralStorageStrategy` there is a single worker so the value returned
    will be all the values on that worker.

    Args:
      value: A value returned by `run()`, `extended.call_for_each_replica()`,
      or a variable created in `scope`.

    Returns:
      A tuple of values contained in `value`. If `value` represents a single
      value, this returns `(value,).`
    """
exit(super(CentralStorageStrategy, self).experimental_local_results(value))
