# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
self.assertEqual(
    "foo/gradients/bar/gradients_0",
    self._grad_source_for_name("foo/gradients/bar/gradients_0/baz"))
