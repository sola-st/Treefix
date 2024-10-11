# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
with ops.device("/cpu:0"):
    t = constant_op.constant([[1., 2.], [0, 0], [3., 4.]])
destination = "/gpu:0"
result = cross_device_utils.copy_tensor_or_indexed_slices_to_device(
    t, destination)

self._assert_values_equal(t, result)
self.assertEqual(device_util.resolve(destination),
                 device_util.resolve(result.device))
