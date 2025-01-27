# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns the list of all local per-replica values contained in `value`.

    Note: This only returns values on the worker initiated by this client.
    When using a `tf.distribute.Strategy` like
    `tf.distribute.experimental.MultiWorkerMirroredStrategy`, each worker
    will be its own client, and this function will only return values
    computed on that worker.

    Args:
      value: A value returned by `experimental_run()`, `run(), or a variable
      created in `scope`.

    Returns:
      A tuple of values contained in `value` where ith element corresponds to
      ith replica. If `value` represents a single value, this returns
      `(value,).`
    """
exit(self._extended._local_results(value))  # pylint: disable=protected-access
