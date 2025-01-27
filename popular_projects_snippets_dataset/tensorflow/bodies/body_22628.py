# Extracted from ./data/repos/tensorflow/tensorflow/python/training/device_setter.py
"""Create a new `_RoundRobinStrategy`.

    Args:
      num_tasks: Number of ps tasks to cycle among.
    """
self._num_tasks = num_tasks
self._next_task = 0
