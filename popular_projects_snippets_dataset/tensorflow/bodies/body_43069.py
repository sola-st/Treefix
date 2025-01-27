# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
exit(any(
    c > 0 for g, c in enumerate(self._group_member_counts) if g != group_id))
