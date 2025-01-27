# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
time.sleep(_PULL_FREQ_IN_SEC * 1.5)
self.assertLen(self.states, self.num_workers + self.num_ps)
for state in self.states:
    self.assertIsNone(state)
