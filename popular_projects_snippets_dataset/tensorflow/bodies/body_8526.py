# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Starts one TensorFlow server for each task in the cluster_resolver.

    It will wait until all the servers are up before returns.
    """
if self._mpr:
    raise ValueError('The cluster has already been started.')
for task_type, task_addresses in self._cluster_spec.items():
    self._start_events[task_type] = []
    self._finish_events[task_type] = []
    for _ in task_addresses:
        self._start_events[task_type].append(self._mpr_manager.Event())
        self._finish_events[task_type].append(self._mpr_manager.Event())

self._mpr = multi_process_runner.MultiProcessRunner(
    self._task_function,
    self._cluster_spec,
    args=(self._start_events, self._finish_events),
    rpc_layer=self._rpc_layer,
    stream_output=self._stream_output,
    return_output=False,
    use_dill_for_args=False)
self._mpr.start()
for task_type, task_addresses in self._cluster_spec.items():
    for i in range(len(task_addresses)):
        self._start_events[task_type][i].wait()
