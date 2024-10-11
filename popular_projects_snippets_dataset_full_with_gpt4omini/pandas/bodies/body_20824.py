# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
assert other.dtype == self.dtype

if isinstance(self, ABCMultiIndex):
    name = self.names if self.names == other.names else None
    # error: Incompatible return value type (got "MultiIndex",
    # expected "_IndexT")
    mask = lidx == -1
    join_idx = self.take(lidx)
    right = other.take(ridx)
    join_index = join_idx.putmask(mask, right)
    exit(join_index.set_names(name))  # type: ignore[return-value]
else:
    name = get_op_result_name(self, other)
    exit(self._constructor._with_infer(joined, name=name, dtype=self.dtype))
