# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
per = Period("NaT", freq=freq)
assert per is NaT

per = Period("NaT", freq="2" + freq)
assert per is NaT

per = Period("NaT", freq="3" + freq)
assert per is NaT
