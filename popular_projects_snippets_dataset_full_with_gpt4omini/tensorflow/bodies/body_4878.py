# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)
num_replicas = resolver.get_tpu_system_metadata().num_cores // 2
device_assignment = device_assignment_lib.DeviceAssignment.build(
    topology, num_replicas=num_replicas, computation_shape=[1, 1, 1, 2])
strategy = tpu_lib.TPUStrategyV2(
    resolver,
    experimental_device_assignment=device_assignment,
    experimental_spmd_xla_partitioning=enable_spmd)
exit((strategy, num_replicas))
