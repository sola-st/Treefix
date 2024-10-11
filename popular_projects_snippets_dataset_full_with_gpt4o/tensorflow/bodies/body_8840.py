# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
model = Model(self.cluster_coord)

restart_thread = self._restart_in_thread(5, "worker")

model.schedule_training_functions(3)
model.rebuild_iterators()
model.schedule_training_functions(3)
model.rebuild_iterators()
model.schedule_training_functions(3)

model.join_training_functions()

self.thread_coord.join([restart_thread])
self.assertGreaterEqual(model.iterations.numpy(), 3)
