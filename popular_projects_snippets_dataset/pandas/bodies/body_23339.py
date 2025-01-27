# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
exit([
    PandasColumn(self._df[name], allow_copy=self._allow_copy)
    for name in self._df.columns
])
