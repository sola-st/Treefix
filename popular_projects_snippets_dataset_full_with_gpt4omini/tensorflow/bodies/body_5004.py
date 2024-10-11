# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
old_context = distribute_coordinator_context.get_current_worker_context()
if old_context:
    raise ValueError(
        "You cannot run distribute coordinator in a `worker_fn`.\t" +
        self._debug_message())
# pylint: disable=protected-access
distribute_coordinator_context._worker_context.current = self
