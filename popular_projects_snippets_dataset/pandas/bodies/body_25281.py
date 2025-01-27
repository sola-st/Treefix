# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
# values might be a 1-d array, or a list-like of arrays.
if is_nested_list_like(values):
    values = [DatetimeConverter._convert_1d(v, unit, axis) for v in values]
else:
    values = DatetimeConverter._convert_1d(values, unit, axis)
exit(values)
