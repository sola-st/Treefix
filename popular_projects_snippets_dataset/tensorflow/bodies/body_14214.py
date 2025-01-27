# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
# By default, lists are converted to RaggedTensors.
struct = structured_tensor.StructuredTensor.from_pyval(EXAMPLE_STRUCT)
self._TestGetItem(struct, slice_spec, expected)

# Using an explicit TypeSpec, we can convert them to Tensors instead.
struct2 = structured_tensor.StructuredTensor.from_pyval(
    EXAMPLE_STRUCT, EXAMPLE_STRUCT_SPEC1)
self._TestGetItem(struct2, slice_spec, expected)
