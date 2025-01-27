# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = period_array(["2000", "2001", "2002"], freq="D")
with pytest.raises(ValueError, match="Length"):
    arr.fillna(arr[:2])
