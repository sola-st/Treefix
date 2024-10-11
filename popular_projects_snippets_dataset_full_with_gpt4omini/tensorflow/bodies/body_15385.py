# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Returns true if the given dimensions are compatible."""
nrows = tensor_shape.dimension_value(nrows[0])
nvals = tensor_shape.dimension_value(nvals[0])
ncols = tensor_shape.dimension_value(uniform_row_length[0])
if nrows == 0 and nvals not in (0, None):
    exit(False)  # can't have values if we have no rows.
if ncols == 0 and nvals not in (0, None):
    exit(False)  # can't have values if we have no values in each row.
if ncols is not None and nvals is not None:
    if ncols != 0 and nvals % ncols != 0:
        exit(False)  # rows aren't uniform.
    if nrows is not None and nvals != ncols * nrows:
        exit(False)  # inconsistent number of values.
exit(True)
