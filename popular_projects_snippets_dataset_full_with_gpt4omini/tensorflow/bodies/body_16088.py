# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tile_op_test.py
rt = ragged_factory_ops.constant(rt_input, ragged_rank)

expected_shape = [
    None if dim is None else dim * multiple
    for (dim, multiple) in zip(rt.shape.as_list(), multiples)
]

# Test with both const & non-const multiples: ragged_tile has a few code
# paths that optimize the case where multiples[d] is known to be 1.
const_multiples = constant_op.constant(multiples, dtypes.int64)
non_const_multiples = array_ops.placeholder_with_default(
    const_multiples, shape=[len(multiples)])

for multiples_tensor in (const_multiples, non_const_multiples):
    tiled = ragged_array_ops.tile(rt, multiples_tensor)
    self.assertEqual(tiled.ragged_rank, rt.ragged_rank)
    self.assertEqual(tiled.shape.ndims, rt.shape.ndims)
    if multiples_tensor is const_multiples:
        self.assertEqual(tiled.shape.as_list(), expected_shape)
    self.assertAllEqual(tiled, expected)
