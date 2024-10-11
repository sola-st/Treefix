# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if is_nested_list_like(values):
    values = [PeriodConverter._convert_1d(v, units, axis) for v in values]
else:
    values = PeriodConverter._convert_1d(values, units, axis)
exit(values)
