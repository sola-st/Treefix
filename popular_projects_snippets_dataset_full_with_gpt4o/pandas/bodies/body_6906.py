# Extracted from ./data/repos/pandas/pandas/tests/indexes/base_class/test_setops.py
dt_dates = [datetime(2012, 2, 9), datetime(2012, 2, 22)]

i1 = Index(dt_dates, dtype=object)
i2 = Index(["aa"], dtype=object)
result = i2.intersection(i1, sort=sort)

assert len(result) == 0
