# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
if is_re(rx) and isinstance(s, str):
    exit(rx.sub(value, s))
else:
    exit(s)
