# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
if expected is None:
    expected = tensor

if context.executing_eagerly():
    exit()  # static shapes are always fully defined in eager mode.

dt = constant_op.constant(tensor)
for ragged_rank in range(1, len(dt.shape) - 1):
    dt_placeholder = array_ops.placeholder_with_default(tensor, tensor_shape)
    rt = RaggedTensor.from_tensor(dt_placeholder, ragged_rank=ragged_rank)
    self.assertIsInstance(rt, RaggedTensor)
    self.assertEqual(rt.ragged_rank, ragged_rank)
    self.assertTrue(
        dt.shape.is_compatible_with(rt.shape),
        '%s is incompatible with %s' % (dt.shape, rt.shape))
    if shape is not None:
        self.assertEqual(rt.shape.as_list(), shape)
    self.assertAllEqual(rt, expected.tolist())
    self.assertAllEqual(rt, RaggedTensor.from_nested_row_splits(
        rt.flat_values, rt.nested_row_splits, validate=True))
