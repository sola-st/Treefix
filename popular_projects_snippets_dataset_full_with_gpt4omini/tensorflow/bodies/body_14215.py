# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_slice_test.py
# By default, lists are converted to RaggedTensors.
if not test_requires_typespec:
    struct_vector = structured_tensor.StructuredTensor.from_pyval(
        EXAMPLE_STRUCT_VECTOR)
    self._TestGetItem(struct_vector, slice_spec, expected)

# Using an explicit TypeSpec, we can convert them to Tensors instead.
struct_vector2 = structured_tensor.StructuredTensor.from_pyval(
    EXAMPLE_STRUCT_VECTOR, EXAMPLE_STRUCT_SPEC1._batch(6))
self._TestGetItem(struct_vector2, slice_spec, expected)
