# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops_test.py
if not (isinstance(a, structured_tensor.StructuredTensor) or
        isinstance(b, structured_tensor.StructuredTensor)):
    exit(super(StructuredArrayOpsTest, self).assertAllEqual(a, b, msg))

if not isinstance(a, structured_tensor.StructuredTensor):
    a = structured_tensor.StructuredTensor.from_pyval(a)
elif not isinstance(b, structured_tensor.StructuredTensor):
    b = structured_tensor.StructuredTensor.from_pyval(b)

try:
    nest.assert_same_structure(a, b, expand_composites=True)
except (TypeError, ValueError) as e:
    self.assertIsNone(e, (msg + ": " if msg else "") + str(e))
a_tensors = [
    x for x in nest.flatten(a, expand_composites=True)
    if isinstance(x, ops.Tensor)
]
b_tensors = [
    x for x in nest.flatten(b, expand_composites=True)
    if isinstance(x, ops.Tensor)
]
self.assertLen(a_tensors, len(b_tensors))
a_arrays, b_arrays = self.evaluate((a_tensors, b_tensors))
for a_array, b_array in zip(a_arrays, b_arrays):
    self.assertAllEqual(a_array, b_array, msg)
