# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_coordinator_test.py
task_type = str(task_type)
task_id = task_id or 0
with self._lock:
    if task_type not in self._std_servers:
        self._std_servers[task_type] = []
    while len(self._std_servers[task_type]) <= task_id:
        self._std_servers[task_type].append(None)

    server = MockServer()
    self._std_servers[task_type][task_id] = server
exit(server)
