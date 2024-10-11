# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
if self.num_workers < 2:
    self.skipTest("Worker number is less than 2.")
model = self._create_model_and_run_indefinitely()

self.assertFalse(self.cluster_coord.done())
self._cluster.kill_task("worker", 0)
self._cluster.kill_task("worker", 1)
time.sleep(2)
self.assertFalse(context.check_alive("/job:worker/replica:0/task:0"))
self.assertFalse(context.check_alive("/job:worker/replica:0/task:1"))
self._cluster.start_task("worker", 0)
self._cluster.start_task("worker", 1)
time.sleep(2)
self.assertTrue(context.check_alive("/job:worker/replica:0/task:0"))
self.assertTrue(context.check_alive("/job:worker/replica:0/task:1"))

model.join_training_functions()
self.assertGreaterEqual(model.iterations.numpy(), 10)
