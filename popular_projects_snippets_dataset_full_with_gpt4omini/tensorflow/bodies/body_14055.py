# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_spec_test.py
if not (isinstance(a, structured_tensor.StructuredTensor) or
        isinstance(b, structured_tensor.StructuredTensor)):
    exit(super(StructuredTensorSpecTest, self).assertAllEqual(a, b, msg))
if not (isinstance(a, structured_tensor.StructuredTensor) and
        isinstance(b, structured_tensor.StructuredTensor)):
    # TODO(edloper) Add support for this once structured_factory_ops is added.
    raise ValueError('Not supported yet')

self.assertEqual(repr(a.shape), repr(b.shape))
self.assertEqual(set(a.field_names()), set(b.field_names()))
for field in a.field_names():
    self.assertAllEqual(a.field_value(field), b.field_value(field))
