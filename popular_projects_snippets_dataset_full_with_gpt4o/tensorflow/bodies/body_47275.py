# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
old_context = get_current_worker_context()
if old_context:
    raise ValueError(
        "You cannot run distribute coordinator in a `worker_fn`.\t" +
        self._debug_message())
# pylint: disable=protected-access
_worker_context.current = self
