# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dr = date_range("2011/1/1", "2012/1/1", freq="W-FRI")
ts = Series(dr)

# it works!
d = DataFrame({"A": "foo", "B": ts}, index=dr)
assert d["B"].isna().all()
