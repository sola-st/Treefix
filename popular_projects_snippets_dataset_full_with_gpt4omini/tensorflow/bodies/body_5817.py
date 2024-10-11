# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py
task_type = task_type if task_type is not None else self._task_type
task_id = task_id if task_id is not None else self._task_id

if task_type is not None and task_id is not None:
    master = self.cluster_spec().task_address(task_type, task_id)
    if rpc_layer or self._rpc_layer:
        exit('%s://%s' % (rpc_layer or self._rpc_layer, master))
    else:
        exit(master)

exit('')
