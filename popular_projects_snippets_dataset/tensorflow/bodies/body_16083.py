# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
dt = constant_op.constant(tensor)
if use_ragged_rank:
    rt = RaggedTensor.from_tensor(dt, lengths, padding, ragged_rank)
else:
    rt = RaggedTensor.from_tensor(dt, lengths, padding)
self.assertEqual(type(rt), RaggedTensor)
self.assertEqual(rt.ragged_rank, ragged_rank)
self.assertTrue(
    dt.shape.is_compatible_with(rt.shape),
    '%s is incompatible with %s' % (dt.shape, rt.shape))
if expected_shape is not None:
    self.assertEqual(rt.shape.as_list(), expected_shape)
self.assertAllEqual(rt, expected)
self.assertAllEqual(rt, RaggedTensor.from_nested_row_splits(
    rt.flat_values, rt.nested_row_splits, validate=True))
