# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t1 = _create_tensor([1, 2], dtype=dtypes.int32)

with self.assertRaisesRegex(
    TypeError,
    r"tensors argument must be a list or a tuple. Got.*EagerTensor"):
    pywrap_tfe.TFE_Py_TensorShapeSlice(t1, -2)
