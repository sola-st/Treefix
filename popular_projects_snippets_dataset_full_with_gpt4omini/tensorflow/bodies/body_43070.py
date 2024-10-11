# Extracted from ./data/repos/tensorflow/tensorflow/python/util/lock_util.py
if group_id < 0 or group_id >= self._num_groups:
    raise ValueError(
        "Argument `group_id` should verify `0 <= group_id < num_groups` "
        f"(with `num_groups={self._num_groups}`). "
        f"Received: group_id={group_id}")
