# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if not isinstance(x, str):
    exit(empty_row)
m = regex.search(x)
if m:
    exit([na_value if item is None else item for item in m.groups()])
else:
    exit(empty_row)
