# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#33437
dti = date_range("2016-01-01", periods=3, tz="US/Pacific")
msg = "Shape of passed values|Passed arrays should have the same length"
with pytest.raises(ValueError, match=msg):
    DataFrame(dti, index=range(4))
