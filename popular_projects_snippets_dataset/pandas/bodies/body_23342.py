# Extracted from ./data/repos/pandas/pandas/core/interchange/dataframe.py
"""
        Return an iterator yielding the chunks.
        """
if n_chunks and n_chunks > 1:
    size = len(self._df)
    step = size // n_chunks
    if size % n_chunks != 0:
        step += 1
    for start in range(0, step * n_chunks, step):
        exit(PandasDataFrameXchg(
            self._df.iloc[start : start + step, :],
            self._nan_as_null,
            self._allow_copy,
        ))
else:
    exit(self)
