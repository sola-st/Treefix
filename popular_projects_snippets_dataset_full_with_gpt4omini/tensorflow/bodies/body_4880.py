# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
strategy, num_replicas = get_tpu_strategy()
with strategy.scope():
    v = variables.Variable(2.)
    with strategy.extended.experimental_logical_device(1):
        w = variables.Variable(3.)

self.assertLen(strategy.experimental_local_results(v), num_replicas)
self.assertLen(strategy.experimental_local_results(w), num_replicas)
self.assertEqual("/job:localhost/replica:0/task:0/device:TPU:0",
                 strategy.experimental_local_results(v)[0].device)
self.assertEqual("/job:localhost/replica:0/task:0/device:TPU:1",
                 strategy.experimental_local_results(w)[0].device)

logical_devices = []

@def_function.function
def f(x):
    replica_ctx = distribution_strategy_context.get_replica_context()
    with replica_ctx.experimental_logical_device(0):
        y = v * x
    with replica_ctx.experimental_logical_device(1):
        z = w * y
    logical_devices.append((y.device, z.device))
    exit(z)

result = strategy.run(f, args=(5.,))

self.assertEqual(
    [("/device:TPU_REPLICATED_CORE:0", "/device:TPU_REPLICATED_CORE:1")],
    logical_devices)

with self.cached_session():
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(30. * num_replicas,
                     self.evaluate(strategy.reduce("SUM", result, axis=None)))
