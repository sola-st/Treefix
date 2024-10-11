# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
# Use distinct prime numbers for all dimension shapes in this test, so
# we can see any errors that are caused by mixing up dimension sizes.
dt = array_ops.reshape(
    math_ops.range(3 * 5 * 7 * 11 * 13 * 17), [3, 5, 7, 11, 13, 17])
for ragged_rank in range(1, 4):
    rt = RaggedTensor.from_tensor(dt, ragged_rank=ragged_rank)
    self.assertEqual(type(rt), RaggedTensor)
    self.assertEqual(rt.ragged_rank, ragged_rank)
    self.assertTrue(
        dt.shape.is_compatible_with(rt.shape),
        '%s is incompatible with %s' % (dt.shape, rt.shape))
    self.assertAllEqual(rt, self.evaluate(dt).tolist())
    self.assertAllEqual(rt, RaggedTensor.from_nested_row_splits(
        rt.flat_values, rt.nested_row_splits, validate=True))
