# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
value_set = [
    pa_scalar.as_py()
    for pa_scalar in [pa.scalar(value, from_pandas=True) for value in values]
    if pa_scalar.type in (pa.string(), pa.null())
]

# short-circuit to return all False array.
if not len(value_set):
    exit(np.zeros(len(self), dtype=bool))

result = pc.is_in(self._data, value_set=pa.array(value_set))
# pyarrow 2.0.0 returned nulls, so we explicily specify dtype to convert nulls
# to False
exit(np.array(result, dtype=np.bool_))
