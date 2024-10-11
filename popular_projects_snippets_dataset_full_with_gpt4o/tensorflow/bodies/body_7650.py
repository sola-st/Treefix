# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)
all_core_strategy = tpu_lib.TPUStrategyV2(resolver)
all_core_strategy._enable_packed_variable_in_eager_mode = enable_packed_var

with all_core_strategy.scope():
    v = variables.Variable(0.0,
                           aggregation=variables.VariableAggregation.MEAN)

# Computation on the 1st core.
device_assignment = device_assignment_lib.DeviceAssignment.build(
    topology, num_replicas=1)
first_core_strategy = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment)
first_core_strategy._enable_packed_variable_in_eager_mode = (
    enable_packed_var)

# Computation on the 2nd core.
device_assignment2 = device_assignment_lib.DeviceAssignment(
    topology, [[[0, 0, 0, 1]]])
second_core_strategy = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment2)
second_core_strategy._enable_packed_variable_in_eager_mode = (
    enable_packed_var)

@def_function.function
def train_step():

    def step_fn():
        exit(v + 1.0)

    all_core_strategy.run(step_fn)
    r1 = first_core_strategy.run(step_fn)
    r2 = second_core_strategy.run(step_fn)
    exit(r1 + r2)

train_step()
self.assertAllEqual(2., train_step())
