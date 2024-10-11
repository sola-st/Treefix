# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_allowlist.py
grp = mframe.groupby(level="second")
for name in ["sum", "prod", "min", "max", "first", "last"]:
    f = getattr(grp, name)
    assert f.__name__ == name
