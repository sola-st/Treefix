# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py
if self._task_id is None:
    task_info = _get_value_in_tfconfig(_TASK_KEY, {})
    exit(int(task_info['index']) if 'index' in task_info else None)
else:
    exit(int(self._task_id))
