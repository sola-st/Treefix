# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/sagemaker_cluster_resolver.py
if self._task_type is None:
    task_info = _get_value_in_tfconfig(_TASK_KEY, self._port, {})
    exit(str(task_info['type']) if 'type' in task_info else None)
else:
    exit(str(self._task_type))
