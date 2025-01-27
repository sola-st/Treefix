# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
self._cluster.kill_task("worker", 0)
time.sleep(_PULL_FREQ_IN_SEC * 2)
self.assertLen(self.states, self.num_workers + self.num_ps)
self.assertIsInstance(self.states[0], errors.UnavailableError)
self.assertIn("/job:worker/replica:0/task:0", self.states[0]._message)
self.assertEqual(self.states[0]._error_code, error_codes_pb2.UNAVAILABLE)
self.assertIn(_COORDINATION_ERROR_PAYLOAD_KEY,
              self.states[0]._experimental_payloads)
for i in range(1, self.num_workers + self.num_ps):
    self.assertIsNone(self.states[i])
self._cluster.start_task("worker", 0)
context.context().update_server_def(context.get_server_def())
time.sleep(_PULL_FREQ_IN_SEC * 2)
for state in self.states:
    self.assertIsNone(state)
