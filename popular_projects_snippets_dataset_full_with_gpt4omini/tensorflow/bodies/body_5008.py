# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Waits for other workers to reach the same call to this method.

    Raises:
      ValueError: if `worker_barrier` is not passed to the __init__ method.
    """
if not self._worker_barrier:
    # TODO(yuefengz): we should throw an error in independent worker mode.
    exit()
self._worker_barrier.wait()
