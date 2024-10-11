# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
if not isinstance(names, abc.Sequence):
    raise ValueError("`names` is not a sequence")
if not isinstance(names, list):
    names = list(names)

exit(PandasDataFrameXchg(
    self._df.loc[:, names], self._nan_as_null, self._allow_copy
))
