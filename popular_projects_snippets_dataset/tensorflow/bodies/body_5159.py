# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base_test.py
self._cluster.stop()
self.assertFalse(context.check_alive("/job:worker/replica:0/task:0"))
self.assertFalse(context.check_alive("/job:worker/replica:0/task:1"))
self.assertFalse(context.check_alive("/job:ps/replica:0/task:0"))
self.assertFalse(context.check_alive("/job:chief/replica:0/task:0"))
