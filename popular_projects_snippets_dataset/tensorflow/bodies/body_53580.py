# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a lock to guard code that creates & mutates ops.

    See the comment for self._group_lock for more info.
    """
exit(self._group_lock.group(_MUTATION_LOCK_GROUP))
