# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base_test.py
self.assertTrue(context.check_alive("/job:worker/replica:0/task:0"))

# It is not allowed to start a task before killing it.
with self.assertRaises(ValueError):
    self._cluster.start_task("worker", 0)

self._cluster.kill_task("worker", 0)
self.assertFalse(context.check_alive("/job:worker/replica:0/task:0"))

# The task is already killed.
with self.assertRaises(ValueError):
    self._cluster.kill_task("worker", 0)

self._cluster.start_task("worker", 0)

# Without a call to update_server_def, the next check_alive will return
# False. Alternatively sleeping for 2 seconds here also works.
context.context().update_server_def(context.get_server_def())

self.assertTrue(context.check_alive("/job:worker/replica:0/task:0"))
