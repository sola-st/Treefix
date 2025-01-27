# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_year.py
with pytest.raises(ValueError, match="Month must go from 1 to 12"):
    YearEnd(month=13)
