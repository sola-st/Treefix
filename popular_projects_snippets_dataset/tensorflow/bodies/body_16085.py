# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
dt = array_ops.zeros(dt_shape)
for ragged_rank in range(1, len(dt_shape) - 1):
    rt = RaggedTensor.from_tensor(dt, lengths, padding, ragged_rank)
    self.assertEqual(type(rt), RaggedTensor)
    self.assertEqual(rt.ragged_rank, ragged_rank)
    self.assertTrue(dt.shape.is_compatible_with(rt.shape))
    self.assertAllEqual(rt, expected)
    self.assertAllEqual(rt, RaggedTensor.from_nested_row_splits(
        rt.flat_values, rt.nested_row_splits, validate=True))
