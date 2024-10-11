# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
# `index` isn't a regular column, and the protocol doesn't support row
# labels - so we export it as Pandas-specific metadata here.
exit({"pandas.index": self._df.index})
