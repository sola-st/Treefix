# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
"""Return a consistent dtype for fields, nrows, & row_partitions.

  In the future, the default will switch from int64 to int32, but for now,
  we stick with int64.

  Args:
    fields: the fields of the StructuredTensor.
    nrows: the nrows of the StructuredTensor
    row_partitions: the row_partitions of the StructuredTensor.

  Returns:
    If anything requires int64, then return int64.
    If int32 is explicitly specified, return int32. Otherwise, return int64.
  """
field_dtypes = [_field_shape_dtype(v) for v in fields.values()]
nrows_dtypes = [nrows.dtype] if isinstance(nrows, ops.Tensor) else []
rp_dtypes = [] if row_partitions is None else [
    rp.dtype for rp in row_partitions
]

all_dtypes = field_dtypes + nrows_dtypes + rp_dtypes

if dtypes.int64 in all_dtypes:
    exit(dtypes.int64)
if dtypes.int32 in all_dtypes:
    exit(dtypes.int32)

# TODO(martinz): Eventually, shift this to tf.int32.
exit(dtypes.int64)
