# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Cast IndexedSlice.indices from int32 to int64 where necessary.

  If `a` and `b` are both IndexedSlices, and their indices have different
  dtypes, then cast both their dtypes to `int64` (modifies `a` and `b`
  in-place).  Otherwise, does nothing.

  Args:
    a: A value, which may be an IndexedSlices.
    b: A value, which may be an IndexedSlices.
  """
if (isinstance(a, indexed_slices.IndexedSlices) and
    isinstance(b, indexed_slices.IndexedSlices) and
    a.indices.dtype != b.indices.dtype):
    # pylint: disable=protected-access
    a._indices = math_ops.cast(a.indices, dtypes.int64)
    b._indices = math_ops.cast(b.indices, dtypes.int64)
