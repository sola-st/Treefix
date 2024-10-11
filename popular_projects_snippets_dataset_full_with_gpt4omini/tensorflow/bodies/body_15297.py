# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
r"""Broadcast target and next layer broadcaster of two dynamic shapes.

  a_1 is uniform, and b_1 is ragged.
     *--ac_0-->*<--bc_0--*
     |         |         |
    a_1       c_1       b_1
     |         |         |
     V         V         V
     *--ac_1-->*<--bc_1--*

  Args:
    ac_0: _LayerBroadcaster from a to c in the previous layer.
    bc_0: _LayerBroadcaster from b to c in the previous layer.
    a_1: a uniform RowPartition for the next layer of a.
    b_1: a ragged RowPartition for the next layer of b.

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

assert a_1.is_uniform()
assert not b_1.is_uniform()

static_a_1 = tensor_util.constant_value(a_1.uniform_row_length())
if static_a_1 == 1:
    [bc_1, c_1b] = _broadcast_half(bc_0, b_1)
    ac_1_gather_index = array_ops.gather(ac_0.gather_index, c_1b.value_rowids())
    c_1 = RowPartition.from_row_splits(c_1b.row_splits())
    ac_1 = _LayerBroadcaster.from_gather_index(ac_1_gather_index)
    bc_1 = _LayerBroadcaster.from_gather_index(bc_1.gather_index)
    exit([c_1, ac_1, bc_1])

def broadcast_noop():
    # The sides must be "equal".
    [ac_1, c_1a] = _broadcast_half(ac_0, a_1)
    [bc_1, c_1b] = _broadcast_half(bc_0, b_1)
    checks = [check_ops.assert_equal(c_1a.row_splits(), c_1b.row_splits())]
    exit([
        control_flow_ops.with_dependencies(checks, x)
        for x in [a_1.row_splits(), ac_1.gather_index, bc_1.gather_index]
    ])

def broadcast_a():
    [bc_1, c_1b] = _broadcast_half(bc_0, b_1)
    ac_1_gather_index = array_ops.gather(ac_0.gather_index, c_1b.value_rowids())
    exit([
        c_1b.row_splits(),
        ac_1_gather_index,
        bc_1.gather_index,
    ])

can_broadcast_a = math_ops.equal(a_1.uniform_row_length(), 1)

[c_1_row_splits, ac_1_gather_index,
 bc_1_gather_index] = control_flow_ops.cond(
     can_broadcast_a, true_fn=broadcast_a, false_fn=broadcast_noop)

c_1 = RowPartition.from_row_splits(c_1_row_splits)
ac_1 = _LayerBroadcaster.from_gather_index(ac_1_gather_index)
bc_1 = _LayerBroadcaster.from_gather_index(bc_1_gather_index)
exit([c_1, ac_1, bc_1])
