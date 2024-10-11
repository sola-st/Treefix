# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
self._cluster.kill_task(task, 0)
self.sleep(1)
self._cluster.start_task(task, 0)
