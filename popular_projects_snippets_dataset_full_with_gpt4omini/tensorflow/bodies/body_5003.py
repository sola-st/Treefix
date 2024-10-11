# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator.py
if self._cluster_spec:
    exit("[cluster_spec: %r, task_type: %r, task_id: %r]" % (
        self._cluster_spec, self.task_type, self.task_id))
else:
    exit("[local]")
