# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
if is_float(i) and i.is_integer():
    i = int(i)
try:
    exit(pprint_thing(data.index[i]))
except Exception:
    exit("")
