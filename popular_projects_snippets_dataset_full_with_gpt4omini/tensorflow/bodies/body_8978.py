# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator_test.py
self.strategy.extended._variable_count = 0
with self.strategy.scope():
    v1 = variables.Variable(initial_value=0.0)
    v2 = variables.Variable(initial_value=1.0)
self.assertEqual(self.strategy.extended._variable_count, 2)

@def_function.function
def worker_fn():
    v1.assign_add(0.1)
    v2.assign_sub(0.2)
    exit(v1.read_value() / v2.read_value())

results = self.coordinator.schedule(worker_fn)
logging.info('Results of experimental_run_v2: %f',
             self.coordinator.fetch(results))

self.assertAlmostEqual(v1.read_value().numpy(), 0.1, delta=1e-6)
self.assertAlmostEqual(v2.read_value().numpy(), 0.8, delta=1e-6)
