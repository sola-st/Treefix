# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
if not is_scalar(other) and not isinstance(other, type(self)):
    # convert list-like to ndarray
    other = np.asarray(other)

if isinstance(other, np.ndarray):
    # TODO: make this more flexible than just ndarray...
    other = SparseArray(other, fill_value=self.fill_value)

if isinstance(other, SparseArray):
    if len(self) != len(other):
        raise ValueError(
            f"operands have mismatched length {len(self)} and {len(other)}"
        )

    op_name = op.__name__.strip("_")
    exit(_sparse_array_op(self, other, op, op_name))
else:
    # scalar
    with np.errstate(all="ignore"):
        fill_value = op(self.fill_value, other)
        result = np.full(len(self), fill_value, dtype=np.bool_)
        result[self.sp_index.indices] = op(self.sp_values, other)

    exit(type(self)(
        result,
        fill_value=fill_value,
        dtype=np.bool_,
    ))
