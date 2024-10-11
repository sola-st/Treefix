# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)

# Strategy for the 1st core.
device_assignment = device_assignment_lib.DeviceAssignment.build(
    topology, num_replicas=1)
first_core_strategy = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment)
first_core_strategy._enable_packed_variable_in_eager_mode = (
    enable_packed_var)

# Strategy for the 2nd core.
device_assignment2 = device_assignment_lib.DeviceAssignment(
    topology, [[[0, 0, 0, 1]]])
second_core_strategy = tpu_lib.TPUStrategyV2(
    resolver, experimental_device_assignment=device_assignment2)
second_core_strategy._enable_packed_variable_in_eager_mode = (
    enable_packed_var)

self.assertLen(first_core_strategy.extended.worker_devices, 1)
self.assertEndsWith(first_core_strategy.extended.worker_devices[0],
                    "device:TPU:0")

self.assertLen(second_core_strategy.extended.worker_devices, 1)
self.assertEndsWith(second_core_strategy.extended.worker_devices[0],
                    "device:TPU:1")
