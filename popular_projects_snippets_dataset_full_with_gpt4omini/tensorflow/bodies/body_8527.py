# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
"""Stops all the servers."""
for task_type, task_addresses in self._cluster_spec.items():
    for i in range(len(task_addresses)):
        self._finish_events[task_type][i].set()
try:
    self._mpr.join()
except multi_process_runner.UnexpectedSubprocessExitError:
    # TODO(yuefengz): investigate why processes exit with 255.
    pass
self._mpr = None
self._start_events = {}
self._finish_events = {}
