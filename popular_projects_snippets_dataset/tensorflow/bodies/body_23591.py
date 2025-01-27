# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/trackable_utils_test.py
with self.assertRaisesRegex(
    ValueError, "Found values in the dependency map which are not keys"):
    trackable_utils.order_by_dependency({1: [2]})
