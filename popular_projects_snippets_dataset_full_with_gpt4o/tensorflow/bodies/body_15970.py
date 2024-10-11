# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_merge_dims_op_test.py
for ragged_rank in ragged_ranks:
    x = ragged_factory_ops.constant(rt, ragged_rank=ragged_rank)

    # Check basic behavior.
    actual = x.merge_dims(outer_axis, inner_axis)
    self.assertAllEqual(expected, actual)
    if outer_axis >= 0 and inner_axis >= 0:
        self.assertEqual(actual.shape.rank,
                         x.shape.rank - (inner_axis - outer_axis))

    # Check behavior with negative axis.
    if outer_axis >= 0 and inner_axis >= 0:
        actual_with_neg_axis = x.merge_dims(outer_axis - x.shape.rank,
                                            inner_axis - x.shape.rank)
        self.assertAllEqual(expected, actual_with_neg_axis)

    # Check behavior with placeholder input (no shape info).
    if (not context.executing_eagerly() and outer_axis >= 0 and
        inner_axis >= 0):
        x_with_placeholders = nest.map_structure(
            lambda t: array_ops.placeholder_with_default(t, None),
            x,
            expand_composites=True)
        actual_with_placeholders = x_with_placeholders.merge_dims(
            outer_axis, inner_axis)
        self.assertAllEqual(expected, actual_with_placeholders)
