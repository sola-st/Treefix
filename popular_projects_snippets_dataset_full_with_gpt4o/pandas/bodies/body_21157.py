# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
op_name = op.__name__

if isinstance(other, SparseArray):
    exit(_sparse_array_op(self, other, op, op_name))

elif is_scalar(other):
    with np.errstate(all="ignore"):
        fill = op(_get_fill(self), np.asarray(other))
        result = op(self.sp_values, other)

    if op_name == "divmod":
        left, right = result
        lfill, rfill = fill
        exit((_wrap_result(op_name, left, self.sp_index, lfill),
            _wrap_result(op_name, right, self.sp_index, rfill),))

    exit(_wrap_result(op_name, result, self.sp_index, fill))

else:
    other = np.asarray(other)
    with np.errstate(all="ignore"):
        if len(self) != len(other):
            raise AssertionError(
                f"length mismatch: {len(self)} vs. {len(other)}"
            )
        if not isinstance(other, SparseArray):
            dtype = getattr(other, "dtype", None)
            other = SparseArray(other, fill_value=self.fill_value, dtype=dtype)
        exit(_sparse_array_op(self, other, op, op_name))
