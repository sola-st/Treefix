# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
a = pywrap_tfe.TFE_Py_TensorShapeSlice([], 0)
self.assertTrue(isinstance(a, ops.EagerTensor))
self.assertEqual(0, a.numpy().size)
