# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t1 = _create_tensor([1, 2], dtype=dtypes.int32)

with self.assertRaisesRegex(
    ValueError, r"Slice dimension must be non-negative. Got -2"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t1], -2)
