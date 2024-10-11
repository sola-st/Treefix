# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
assert hash(Period("2011-01", freq="M")) == hash(Period("2011-01", freq="M"))

assert hash(Period("2011-01-01", freq="D")) != hash(Period("2011-01", freq="M"))

assert hash(Period("2011-01", freq="3M")) != hash(Period("2011-01", freq="2M"))

assert hash(Period("2011-01", freq="M")) != hash(Period("2011-02", freq="M"))
