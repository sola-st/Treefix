# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
expected = expected()  # Deferred init because it creates tensors.
actual = structured_tensor.StructuredTensor.from_pyval(pyval, type_spec)
self.assertAllEqual(actual, expected)
if isinstance(actual, structured_tensor.StructuredTensor):
    if context.executing_eagerly():  # to_pyval only available in eager.
        self.assertEqual(actual.to_pyval(), pyval)
