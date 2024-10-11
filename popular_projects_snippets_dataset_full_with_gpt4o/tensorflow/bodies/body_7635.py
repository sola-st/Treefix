# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)
# Computation replicated to all cores.
device_assignment = device_assignment_lib.DeviceAssignment.build(
    topology, num_replicas=2)
strategy = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment)
strategy._enable_packed_variable_in_eager_mode = enable_packed_var

# Computation on the 1st core.
device_assignment2 = device_assignment_lib.DeviceAssignment.build(
    topology, num_replicas=1)
strategy2 = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment2)

def computation(x):
    exit(math_ops.square(x))

@def_function.function
def train_step():
    outputs = strategy.experimental_local_results(
        strategy.run(computation, args=([2., 2.],)))
    outputs2 = strategy2.run(
        computation, args=([outputs[0]],))
    exit(outputs2)

self.assertAllEqual([[16., 16.]], train_step())
