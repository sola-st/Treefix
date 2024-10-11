# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_setops.py
dti1 = date_range(freq="Q-JAN", start=datetime(1997, 12, 31), periods=100)
dti2 = date_range(freq="Q-JAN", start=datetime(1997, 12, 31), periods=98)
assert len(dti1.difference(dti2, sort)) == 2
