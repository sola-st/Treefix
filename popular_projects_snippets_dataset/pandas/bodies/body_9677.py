# Extracted from ./data/repos/pandas/pandas/tests/arrays/period/test_constructors.py
with pytest.raises(IncompatibleFrequency, match=msg):
    period_array(data, freq)
