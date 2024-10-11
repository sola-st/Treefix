# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
r"""Broadcast target and next layer broadcaster of two dynamic shapes.

     *--ac_0-->*<--bc_0--*
     |         |         |
    a_1       c_1       b_1
     |         |         |
     V         V         V
     *--ac_1-->*<--bc_1--*

  Args:
    ac_0: _LayerBroadcaster from a to c in the previous layer.
    bc_0: _LayerBroadcaster from b to c in the previous layer.
    a_1: a RowPartition for the next layer of a.
    b_1: a RowPartition for the next layer of b.

  Returns:
    (c_1, ac_1, bc_1)
    c_1: a RowPartition for the next layer of the dynamic shape.
    ac_1: _LayerBroadcaster from a to c in the next layer.
    bc_1: _LayerBroadcaster from b to c in the next layer.
  """
if not isinstance(ac_0, _LayerBroadcaster):
    raise TypeError("ac_0 should be a _LayerBroadcaster")
if not isinstance(bc_0, _LayerBroadcaster):
    raise TypeError("bc_0 should be a _LayerBroadcaster")
if not isinstance(a_1, RowPartition):
    raise TypeError("a_1 should be a RowPartition")
if not isinstance(b_1, RowPartition):
    raise TypeError("b_1 should be a RowPartition")

if a_1.is_uniform():
    if b_1.is_uniform():
        exit(_broadcast_dynamic_shape_next_layer_both_uniform(
            ac_0, bc_0, a_1, b_1))
    else:
        exit(_broadcast_dynamic_shape_next_layer_half_ragged(
            ac_0, bc_0, a_1, b_1))
else:
    if b_1.is_uniform():
        [c_1, bc_1, ac_1] = _broadcast_dynamic_shape_next_layer_half_ragged(  # pylint: disable=arguments-out-of-order
            bc_0, ac_0, b_1, a_1)
        exit((c_1, ac_1, bc_1))
    else:
        # If neither shape is uniform, we cannot broadcast the dimension.
        [ac_1, c_1a] = _broadcast_half(ac_0, a_1)
        [bc_1, c_1b] = _broadcast_half(bc_0, b_1)
        check_valid = [
            check_ops.assert_equal(c_1a.row_splits(), c_1b.row_splits())
        ]
        exit((c_1a._with_dependencies(check_valid),  # pylint: disable=protected-access
            ac_1.with_dependencies(check_valid),
            bc_1.with_dependencies(check_valid)))
