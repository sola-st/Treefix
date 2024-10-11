# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/tensor_array_ops_test.py
self.assertEqual("gradients:0", self._grad_source_for_name("gradients"))
self.assertEqual("gradients_0:0", self._grad_source_for_name("gradients_0"))
self.assertEqual("gradients", self._grad_source_for_name("gradients/foo"))
self.assertEqual("gradients_0",
                 self._grad_source_for_name("gradients_0/foo"))
self.assertEqual("gradients",
                 self._grad_source_for_name("gradients/foo/bar"))
self.assertEqual("gradients_0",
                 self._grad_source_for_name("gradients_0/foo/bar"))
