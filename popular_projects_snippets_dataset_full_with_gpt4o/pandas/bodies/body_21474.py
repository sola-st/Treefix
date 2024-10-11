# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
# short-circuit to return all False array.
if not len(values):
    exit(np.zeros(len(self), dtype=bool))

result = pc.is_in(self._data, value_set=pa.array(values, from_pandas=True))
# pyarrow 2.0.0 returned nulls, so we explicitly specify dtype to convert nulls
# to False
exit(np.array(result, dtype=np.bool_))
