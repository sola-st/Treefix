# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
if not isinstance(indices, abc.Sequence):
    raise ValueError("`indices` is not a sequence")
if not isinstance(indices, list):
    indices = list(indices)

exit(PandasDataFrameXchg(
    self._df.iloc[:, indices], self._nan_as_null, self._allow_copy
))
