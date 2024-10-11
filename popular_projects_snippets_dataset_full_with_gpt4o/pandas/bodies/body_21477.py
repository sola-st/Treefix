# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
raise NotImplementedError(
    f"{type(self)} does not support reshape "
    f"as backed by a 1D pyarrow.ChunkedArray."
)
