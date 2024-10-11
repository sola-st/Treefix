# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
with self.assertRaises(ValueError):
    self._grad_source_for_name("")
with self.assertRaises(ValueError):
    self._grad_source_for_name("foo")
with self.assertRaises(ValueError):
    self._grad_source_for_name("foo/bar")
