# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
if method == "attr":
    exit(getattr(gb, op)(**kwargs))
else:
    exit(getattr(gb, method)(op, **kwargs))
