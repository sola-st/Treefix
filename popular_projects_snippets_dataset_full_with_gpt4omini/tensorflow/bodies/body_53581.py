# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a lock to guard code for Session.run.

    See the comment for self._group_lock for more info.
    """
exit(self._group_lock.group(_SESSION_RUN_LOCK_GROUP))
