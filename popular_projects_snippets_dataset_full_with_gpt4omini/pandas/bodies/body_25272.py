# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
if isinstance(d, str):
    parsed = Timestamp(d)
    exit(_to_ordinalf(parsed.time()))
if isinstance(d, pydt.time):
    exit(_to_ordinalf(d))
exit(d)
