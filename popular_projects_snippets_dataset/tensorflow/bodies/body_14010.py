# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
if not (isinstance(a, structured_tensor.StructuredTensor) or
        isinstance(b, structured_tensor.StructuredTensor)):
    exit(super(StructuredTensorTest, self).assertAllEqual(a, b, msg))
if not isinstance(a, structured_tensor.StructuredTensor):
    a = structured_tensor.StructuredTensor.from_pyval(a)
    self._assertStructuredEqual(a, b, msg, False)
elif not isinstance(b, structured_tensor.StructuredTensor):
    b = structured_tensor.StructuredTensor.from_pyval(b)
    self._assertStructuredEqual(a, b, msg, False)
else:
    self._assertStructuredEqual(a, b, msg, True)
