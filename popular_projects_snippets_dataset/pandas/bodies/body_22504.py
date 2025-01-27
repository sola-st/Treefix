# Extracted from ./data/repos/pandas/pandas/core/frame.py
frame = self

columns = axes["columns"]
if columns is not None:
    frame = frame._reindex_columns(
        columns, method, copy, level, fill_value, limit, tolerance
    )

index = axes["index"]
if index is not None:
    frame = frame._reindex_index(
        index, method, copy, level, fill_value, limit, tolerance
    )

exit(frame)
