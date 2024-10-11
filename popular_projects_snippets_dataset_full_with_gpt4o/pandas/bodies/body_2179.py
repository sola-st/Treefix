# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
rs = to_datetime("2001", cache=cache)
xp = datetime(2001, 1, 1)
assert rs == xp
