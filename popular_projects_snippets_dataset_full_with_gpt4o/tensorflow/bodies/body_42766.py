# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t1 = _create_tensor([[1, 2], [3, 4], [5, 6]], dtype=dtypes.int32)
t2 = _create_tensor([1, 2], dtype=dtypes.int32)
t3 = _create_tensor(2, dtype=dtypes.int32)

with self.assertRaisesRegex(
    IndexError,
    r"Slice dimension \(2\) must be smaller than rank of all tensors, "
    "but tensor at index 0 has rank 2"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t1], 2)

with self.assertRaisesRegex(
    IndexError,
    r"Slice dimension \(1\) must be smaller than rank of all tensors, "
    "but tensor at index 0 has rank 1"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t2], 1)

with self.assertRaisesRegex(
    IndexError,
    r"Slice dimension \(1\) must be smaller than rank of all tensors, "
    "but tensor at index 1 has rank 1"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t1, t2], 1)

with self.assertRaisesRegex(
    IndexError,
    r"Slice dimension \(0\) must be smaller than rank of all tensors, "
    "but tensor at index 0 has rank 0"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t3], 0)

with self.assertRaisesRegex(
    IndexError,
    r"Slice dimension \(0\) must be smaller than rank of all tensors, "
    "but tensor at index 2 has rank 0"):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t2, t1, t3], 0)
