# Extracted from ./data/repos/pandas/pandas/core/frame.py
axis = self._get_axis_number(axis)
if numeric_only:
    data = self._get_numeric_data()
else:
    data = self

res = data._reduce(
    nanops.nanargmin, "argmin", axis=axis, skipna=skipna, numeric_only=False
)
indices = res._values

# indices will always be np.ndarray since axis is not None and
# values is a 2d array for DataFrame
# error: Item "int" of "Union[int, Any]" has no attribute "__iter__"
assert isinstance(indices, np.ndarray)  # for mypy

index = data._get_axis(axis)
result = [index[i] if i >= 0 else np.nan for i in indices]
final_result = data._constructor_sliced(result, index=data._get_agg_axis(axis))
exit(final_result.__finalize__(self, method="idxmin"))
