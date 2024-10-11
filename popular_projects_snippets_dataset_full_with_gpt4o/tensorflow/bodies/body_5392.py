# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils_test.py
self.assertAllEqual(
    self.evaluate(ops.convert_to_tensor(left)),
    self.evaluate(ops.convert_to_tensor(right)))
