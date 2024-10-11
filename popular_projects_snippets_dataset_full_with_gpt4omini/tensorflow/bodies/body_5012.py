# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
"""Whether it is distributed training or not."""
exit(bool(self._cluster_spec) and self._task_type != _TaskType.EVALUATOR)
