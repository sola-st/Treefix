# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = self._create_model_and_run_indefinitely()

self.assertFalse(self.cluster_coord.done())
self._cluster.kill_task("worker", 0)
time.sleep(2)
self.assertFalse(context.check_alive("/job:worker/replica:0/task:0"))
self._cluster.start_task("worker", 0)
time.sleep(2)
self.assertTrue(context.check_alive("/job:worker/replica:0/task:0"))
self._cluster.kill_task("worker", 0)
time.sleep(2)
self.assertFalse(context.check_alive("/job:worker/replica:0/task:0"))
self._cluster.start_task("worker", 0)
time.sleep(2)
self.assertTrue(context.check_alive("/job:worker/replica:0/task:0"))

model.join_training_functions()
self.assertGreaterEqual(model.iterations.numpy(), 10)
