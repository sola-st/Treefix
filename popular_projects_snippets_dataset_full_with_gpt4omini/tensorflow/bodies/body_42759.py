# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t1 = _create_tensor([[1, 2], [3, 4], [5, 6]], dtype=dtypes.int32)
t2 = _create_tensor([[1, 2, 5], [3, 4, 5]], dtype=dtypes.int32)
t3 = _create_tensor([[1], [3], [5], [6]], dtype=dtypes.int32)

r = pywrap_tfe.TFE_Py_TensorShapeSlice([t1, t2, t3], 0)
self.assertAllEqual(np.array([3, 2, 4]), r.numpy())

r = pywrap_tfe.TFE_Py_TensorShapeSlice([t1, t2, t3], 1)
self.assertAllEqual(np.array([2, 3, 1]), r.numpy())
