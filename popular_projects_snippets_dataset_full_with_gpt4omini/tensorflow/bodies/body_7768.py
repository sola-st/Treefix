# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
resolver = get_tpu_cluster_resolver()
remote.connect_to_cluster(resolver)
topology = tpu_strategy_util.initialize_tpu_system(resolver)
device_assignment = device_assignment_lib.DeviceAssignment(
    topology, core_assignment=[[[0, 0, 0, 0]]])
self.assertAllEqual([[[0, 0, 0, 0]]], device_assignment.core_assignment)
self.assertEqual(1, device_assignment.num_cores_per_replica)
self.assertEqual(1, device_assignment.num_replicas)
self.assertEqual("/task:0/device:TPU:0", device_assignment.tpu_device())
self.assertEqual("/task:0/device:CPU:0", device_assignment.host_device())
