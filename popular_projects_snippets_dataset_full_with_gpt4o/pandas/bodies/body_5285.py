# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
i1 = Period("1982", freq="Min")
assert i1.freq == offsets.Minute()
assert i1.freqstr == "T"
