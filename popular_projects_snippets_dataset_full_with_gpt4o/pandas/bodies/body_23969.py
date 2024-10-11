# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""we are going to write this as a frame table"""
if not isinstance(obj, DataFrame):
    name = obj.name or "values"
    obj = obj.to_frame(name)
exit(super().write(obj=obj, data_columns=obj.columns.tolist(), **kwargs))
