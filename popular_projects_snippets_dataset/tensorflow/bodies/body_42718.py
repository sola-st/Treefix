# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
self.assertFalse(bool(_create_tensor(False)))
self.assertFalse(bool(_create_tensor([False])))
self.assertFalse(bool(_create_tensor([[False]])))
self.assertFalse(bool(_create_tensor([0])))
self.assertFalse(bool(_create_tensor([0.])))
self.assertTrue(bool(_create_tensor([1])))
self.assertTrue(bool(_create_tensor([1.])))
