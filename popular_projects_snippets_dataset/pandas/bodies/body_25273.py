# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
valid_types = (str, pydt.time)
if isinstance(value, valid_types) or is_integer(value) or is_float(value):
    exit(time2num(value))
if isinstance(value, Index):
    exit(value.map(time2num))
if isinstance(value, (list, tuple, np.ndarray, Index)):
    exit([time2num(x) for x in value])
exit(value)
