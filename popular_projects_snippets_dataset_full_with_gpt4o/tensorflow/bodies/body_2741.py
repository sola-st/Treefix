# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
shape = (3, 4)
device_assignment = xla_client.DeviceAssignment.create(
    np.arange(np.prod(shape)).reshape(*shape))
self.assertEqual(device_assignment.replica_count(), shape[0])
self.assertEqual(device_assignment.computation_count(), shape[1])
serialized = device_assignment.serialize()
self.assertIsInstance(serialized, bytes)
self.assertNotEmpty(serialized)
