# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
self.assertIsInstance(left, indexed_slices_lib.IndexedSlices)
self.assertIsInstance(right, indexed_slices_lib.IndexedSlices)
self.assertEqual(
    device_util.resolve(left.device), device_util.resolve(right.device))
self.assertAllEqual(
    self.evaluate(ops.convert_to_tensor(left)),
    self.evaluate(ops.convert_to_tensor(right)))
