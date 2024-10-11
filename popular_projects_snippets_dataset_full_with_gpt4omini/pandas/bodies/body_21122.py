# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py

if not len(self) or periods == 0:
    exit(self.copy())

if isna(fill_value):
    fill_value = self.dtype.na_value

subtype = np.result_type(fill_value, self.dtype.subtype)

if subtype != self.dtype.subtype:
    # just coerce up front
    arr = self.astype(SparseDtype(subtype, self.fill_value))
else:
    arr = self

empty = self._from_sequence(
    [fill_value] * min(abs(periods), len(self)), dtype=arr.dtype
)

if periods > 0:
    a = empty
    b = arr[:-periods]
else:
    a = arr[abs(periods) :]
    b = empty
exit(arr._concat_same_type([a, b]))
