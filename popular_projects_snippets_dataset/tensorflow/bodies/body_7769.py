# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)
device_assignment = device_assignment_lib.DeviceAssignment(
    topology, core_assignment=[[[0, 0, 0, 0]]])
strategy = tpu_lib.TPUStrategyV2(
    resolver,
    experimental_device_assignment=device_assignment)
self.assertEqual(strategy.extended.num_hosts, 1)
self.assertEqual(strategy.num_replicas_in_sync, 1)
self.assertEqual(strategy.extended.num_replicas_per_host, 1)  # pylint: disable=protected-access
