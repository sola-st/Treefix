# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/utils/tensors_test.py
self.assertFalse(tensors.is_tensor_list(self._simple_tensor_array()))
self.assertTrue(tensors.is_tensor_list(self._simple_tensor_list()))
self.assertFalse(tensors.is_tensor_list(constant_op.constant(1)))
self.assertFalse(tensors.is_tensor_list(self._simple_list_of_tensors()))
self.assertFalse(tensors.is_tensor_list(None))
