# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Constructs a new RowPartitionSpec.

    Args:
      nrows: The number of rows in the RowPartition, or `None` if unspecified.
      nvals: The number of values partitioned by the RowPartition, or `None` if
        unspecified.
      uniform_row_length: The number of values in each row for this
        RowPartition, or `None` if rows are ragged or row length is unspecified.
      dtype: The data type used to encode the partition.  One of `tf.int64` or
        `tf.int32`.
    """
# Wrap dimension sizes in 1D TensorShapes so the default implementations
# of TypeSpec methods such as `is_compatile_with` will work.
nrows = tensor_shape.TensorShape([nrows])
nvals = tensor_shape.TensorShape([nvals])
if not isinstance(uniform_row_length, tensor_shape.TensorShape):
    uniform_row_length = tensor_shape.TensorShape([uniform_row_length])
else:
    uniform_row_length = uniform_row_length.with_rank(1)

self._nrows = nrows
self._nvals = nvals
self._uniform_row_length = uniform_row_length
self._dtype = dtypes.as_dtype(dtype)
if self._dtype not in (dtypes.int32, dtypes.int64):
    raise ValueError("dtype must be tf.int32 or tf.int64")

# Check dimension consistency, & infer dimensions when possible.
nrows = tensor_shape.dimension_value(nrows[0])
nvals = tensor_shape.dimension_value(nvals[0])
ncols = tensor_shape.dimension_value(uniform_row_length[0])
if nrows == 0:  # no rows -> no values.
    if nvals is None:
        self._nvals = tensor_shape.TensorShape([0])
    elif nvals != 0:
        raise ValueError("nvals=%s is not compatible with nrows=%s" %
                         (nvals, nrows))
if ncols == 0:  # there are no values in each row -> no values.
    if nvals is None:
        self._nvals = tensor_shape.TensorShape([0])
    elif nvals != 0:
        raise ValueError("nvals=%s is not compatible with uniform_row_length"
                         "=%s" % (nvals, uniform_row_length))
if ncols is not None and nvals is not None:
    if ncols != 0 and nvals % ncols != 0:
        raise ValueError("nvals=%s is not compatible with uniform_row_length"
                         "=%s (doesn't divide evenly)" % (nvals, ncols))
    if nrows is not None and nvals != ncols * nrows:
        raise ValueError("nvals=%s is not compatible with nrows=%s and "
                         "uniform_row_length=%s" % (nvals, nrows, ncols))
    if nrows is None and ncols != 0:
        self._nrows = tensor_shape.TensorShape([nvals // ncols])
if ncols is not None and nrows is not None and nvals is None:
    self._nvals = tensor_shape.TensorShape([ncols * nrows])
