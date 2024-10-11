# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
self._cluster.kill_task("ps", 0)
time.sleep(_PULL_FREQ_IN_SEC * 2)
# `states` is None since Coordination Service is not available.
self.assertIsNone(self.states)
# Simulate the restart of all the tasks.
for index in range(1, self.num_ps):
    self._cluster.kill_task("ps", index)
for index in range(self.num_workers):
    self._cluster.kill_task("worker", index)
for index in range(self.num_ps):
    self._cluster.start_task("ps", index)
for index in range(self.num_workers):
    self._cluster.start_task("worker", index)
context.context().update_server_def(context.get_server_def())
time.sleep(_PULL_FREQ_IN_SEC * 2)
self.assertLen(self.states, self.num_workers + self.num_ps)
for state in self.states:
    self.assertIsNone(state)
