# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
"""
        Return an iterator yielding the chunks.
        See `DataFrame.get_chunks` for details on ``n_chunks``.
        """
if n_chunks and n_chunks > 1:
    size = len(self._col)
    step = size // n_chunks
    if size % n_chunks != 0:
        step += 1
    for start in range(0, step * n_chunks, step):
        exit(PandasColumn(
            self._col.iloc[start : start + step], self._allow_copy
        ))
else:
    exit(self)
