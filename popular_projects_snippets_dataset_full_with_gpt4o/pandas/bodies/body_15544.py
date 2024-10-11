# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_between.py
# GH 40628
series = Series(date_range("1/1/2000", periods=10))
left, right = series[[2, 7]]

value_error_msg = (
    "Inclusive has to be either string of 'both',"
    "'left', 'right', or 'neither'."
)

with pytest.raises(ValueError, match=value_error_msg):
    series = Series(date_range("1/1/2000", periods=10))
    series.between(left, right, inclusive=inclusive)
