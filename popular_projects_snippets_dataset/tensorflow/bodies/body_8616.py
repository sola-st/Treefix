# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parallel_device/parallel_device_test.py
"""Asserts that replication of `computation` works and is equivalent."""
with self.device:
    parallel_result = computation()
non_parallel_result = computation()
# The computations should have the same number and structure of Tensor
# objects, even though the tensors themselves will be on different devices
# and represent different numbers of values.
nest.assert_same_structure(parallel_result, non_parallel_result)
non_parallel_flat = nest.flatten(non_parallel_result)
parallel_flat = nest.flatten(parallel_result)
self.assertGreater(len(parallel_flat), 0)
for non_parallel, parallel in zip(non_parallel_flat, parallel_flat):
    self.assertEqual(self.device._name, parallel.device)
    self.assertNotEqual(self.device._name, non_parallel.device)
    for parallel_component in self.device.unpack(parallel):
        self.assertAllClose(non_parallel, parallel_component)
