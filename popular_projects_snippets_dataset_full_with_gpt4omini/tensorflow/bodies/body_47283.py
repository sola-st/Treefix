# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/distribute/distribute_coordinator_utils.py
"""Whether it is distributed training or not."""
exit(bool(self._cluster_spec) and self._task_type != _TaskType.EVALUATOR)
