# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
"""Dumps the propoerties of each worker context.

    It dumps the context properties to a dict mapping from task_type to a list
    of tuples of master_target, num_workers, is_chief and distribute_mode, where
    the list is indexed by the task_id.

    Args:
      strategy: a `DistributionStrategy` object.
    """
context = distribute_coordinator_context.get_current_worker_context()
self.assertTrue(context is not None)
task_type = str(context.task_type)
task_id = context.task_id or 0
with self._lock:
    if task_type not in self._worker_context:
        self._worker_context[task_type] = []
    while len(self._worker_context[task_type]) <= task_id:
        self._worker_context[task_type].append(None)
    self._worker_context[task_type][task_id] = (context.master_target,
                                                context.num_workers,
                                                context.is_chief,
                                                context.distributed_mode)
