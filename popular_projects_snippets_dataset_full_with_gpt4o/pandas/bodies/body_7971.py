# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
msg = "start and end must not be NaT"
with pytest.raises(ValueError, match=msg):
    period_range(start="NaT", end="2011-01-01", freq="M")
with pytest.raises(ValueError, match=msg):
    period_range(start="2011-01-01", end="NaT", freq="M")
