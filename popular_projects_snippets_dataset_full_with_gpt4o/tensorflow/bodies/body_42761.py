# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t1 = _create_tensor([1, 2], dtype=dtypes.int32)

with self.assertRaisesRegex(
    TypeError,
    r"Expected a list of EagerTensors but element 1 has type \"str\""):
    pywrap_tfe.TFE_Py_TensorShapeSlice([t1, "abc"], 0)

with self.assertRaisesRegex(
    TypeError,
    r"Expected a list of EagerTensors but element 0 has type \"int\""):
    pywrap_tfe.TFE_Py_TensorShapeSlice([2, t1], 0)
