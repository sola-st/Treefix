# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linear_operator_zeros.py
"""Static check of init arg `num_rows`, possibly add asserts."""
# Possibly add asserts.
if self._assert_proper_shapes:
    self._num_rows = control_flow_ops.with_dependencies([
        check_ops.assert_rank(
            self._num_rows,
            0,
            message="Argument num_rows must be a 0-D Tensor."),
        check_ops.assert_non_negative(
            self._num_rows,
            message="Argument num_rows must be non-negative."),
    ], self._num_rows)
    self._num_columns = control_flow_ops.with_dependencies([
        check_ops.assert_rank(
            self._num_columns,
            0,
            message="Argument num_columns must be a 0-D Tensor."),
        check_ops.assert_non_negative(
            self._num_columns,
            message="Argument num_columns must be non-negative."),
    ], self._num_columns)

# Static checks.
if not self._num_rows.dtype.is_integer:
    raise TypeError("Argument num_rows must be integer type.  Found:"
                    " %s" % self._num_rows)

if not self._num_columns.dtype.is_integer:
    raise TypeError("Argument num_columns must be integer type.  Found:"
                    " %s" % self._num_columns)

num_rows_static = self._num_rows_static
num_columns_static = self._num_columns_static

if num_rows_static is not None:
    if num_rows_static.ndim != 0:
        raise ValueError("Argument num_rows must be a 0-D Tensor.  Found:"
                         " %s" % num_rows_static)

    if num_rows_static < 0:
        raise ValueError("Argument num_rows must be non-negative.  Found:"
                         " %s" % num_rows_static)
if num_columns_static is not None:
    if num_columns_static.ndim != 0:
        raise ValueError("Argument num_columns must be a 0-D Tensor.  Found:"
                         " %s" % num_columns_static)

    if num_columns_static < 0:
        raise ValueError("Argument num_columns must be non-negative.  Found:"
                         " %s" % num_columns_static)
