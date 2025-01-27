# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
super().__init__(obj, n, keep)
if not is_list_like(columns) or isinstance(columns, tuple):
    columns = [columns]

columns = cast(Sequence[Hashable], columns)
columns = list(columns)
self.columns = columns
