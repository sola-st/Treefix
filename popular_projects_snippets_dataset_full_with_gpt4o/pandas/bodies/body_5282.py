# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
# GH#3363
p = Period("2000-1-1 12:34:12", freq="S")
res = p.strftime("%Y-%m-%d %H:%M:%S")
assert res == "2000-01-01 12:34:12"
assert isinstance(res, str)
