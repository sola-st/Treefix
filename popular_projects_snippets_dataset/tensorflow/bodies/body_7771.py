# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)

strategy0 = tpu_lib.TPUStrategyV2(resolver)
self.assertEqual(
    ("/job:localhost/replica:0/task:0/device:TPU:0",
     "/job:localhost/replica:0/task:0/device:TPU:1"),
    strategy0.extended.worker_devices)

with strategy0.scope():
    v = variables.Variable(1.)

v1_assign_op = strategy0.experimental_local_results(v)[1].assign(42.)

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.evaluate(v1_assign_op)
    self.assertAllEqual([1., 42.],
                        self.evaluate(
                            strategy0.experimental_local_results(v)))

# Second strategy has devices reversed relative to the first.
device_assignment = device_assignment_lib.DeviceAssignment(
    topology, core_assignment=[[[0, 0, 0, 1]], [[0, 0, 0, 0]]])
strategy1 = tpu_lib.TPUStrategyV2(
    resolver,
    experimental_device_assignment=device_assignment)
self.assertEqual(
    ("/job:localhost/replica:0/task:0/device:TPU:1",
     "/job:localhost/replica:0/task:0/device:TPU:0"),
    strategy1.extended.worker_devices)

v_read = strategy1.run(def_function.function(v.read_value))

with self.cached_session():
    self.assertAllEqual([42., 1.],
                        self.evaluate(
                            strategy0.experimental_local_results(v_read)))
