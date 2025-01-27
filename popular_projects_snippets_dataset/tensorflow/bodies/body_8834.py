# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = Model(self.cluster_coord)
model.schedule_training_functions(2)
model.join_training_functions()
self.assertEqual(model.iterations.numpy(), 2)

self._restart(downtime_secs=2, job="worker")

model.schedule_training_functions(2)
model.join_training_functions()
self.assertEqual(model.iterations.numpy(), 4)
