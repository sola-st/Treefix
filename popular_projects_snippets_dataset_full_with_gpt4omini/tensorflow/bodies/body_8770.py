# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/get_task_states_test.py
super().tearDown()
self.polling_thread.stop()
self._cluster.stop()
self._cluster = None
