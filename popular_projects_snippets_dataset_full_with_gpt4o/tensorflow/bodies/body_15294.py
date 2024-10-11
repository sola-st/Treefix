# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
"""Does a NOOP broadcast of a_1.

      *-ac_0-->*
      |        |
     a_1      c_1
      |        |
      V        V
      *-ac_1-->*

  Note that by definition this cannot fail: there is always a well-defined
  NOOP broadcast. This is usually intended as half of broadcasting two shapes
  together.
  Args:
    ac_0: previous LayerBroadcaster
    a_1: previous RowPartition

  Returns:
    [ac_1, c_1] where ac_1 is the next LayerBroadcaster, and c_1 is the
    broadcast RowPartition
  """
c_1 = ac_0.broadcast_row_partition(a_1)
old_value_rowids = array_ops.gather(ac_0.gather_index, c_1.value_rowids())
old_row_starts = array_ops.gather(a_1.row_splits(), old_value_rowids)
gather_index = old_row_starts + c_1.offsets_in_rows()
exit([_LayerBroadcaster.from_gather_index(gather_index), c_1])
