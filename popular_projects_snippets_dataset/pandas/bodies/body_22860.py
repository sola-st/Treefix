# Extracted from ./data/repos/pandas/pandas/core/array_algos/replace.py
if is_re(rx) and isinstance(s, str):
    exit(value if rx.search(s) is not None else s)
else:
    exit(s)
