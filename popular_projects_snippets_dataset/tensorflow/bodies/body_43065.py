# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
"""Initialize a group lock.

    Args:
      num_groups: The number of groups that will be accessing the resource under
        consideration. Should be a positive number.

    Returns:
      A group lock that can then be used to synchronize code.

    Raises:
      ValueError: If num_groups is less than 1.
    """
if num_groups < 1:
    raise ValueError(
        "Argument `num_groups` must be a positive integer. "
        f"Received: num_groups={num_groups}")
self._ready = threading.Condition(threading.Lock())
self._num_groups = num_groups
self._group_member_counts = [0] * self._num_groups
