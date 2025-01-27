# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
struct = structured_tensor.StructuredTensor.from_pyval(
    EXAMPLE_STRUCT_VECTOR)
with self.assertRaisesRegex(exception, error):
    struct.__getitem__(slice_spec)
