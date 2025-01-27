# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
self.assertEqual("foo/gradients:0",
                 self._grad_source_for_name("foo/gradients"))
self.assertEqual("foo/gradients_0:0",
                 self._grad_source_for_name("foo/gradients_0"))
self.assertEqual("foo/gradients",
                 self._grad_source_for_name("foo/gradients/bar"))
self.assertEqual("foo/gradients_0",
                 self._grad_source_for_name("foo/gradients_0/bar"))
self.assertEqual("foo/bar/gradients",
                 self._grad_source_for_name("foo/bar/gradients/baz"))
self.assertEqual("foo/bar/gradients_0",
                 self._grad_source_for_name("foo/bar/gradients_0/baz"))
