# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Initializes the barrier object.

    Args:
      num_participants: an integer which is the expected number of calls of
        `wait` pass to through this barrier.
    """
self._num_participants = num_participants
self._counter = 0
self._flag = False
self._local_sense = threading.local()
self._lock = threading.Lock()
self._condition = threading.Condition()
