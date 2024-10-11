# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
# Week with weekday should raise TypeError and _not_ AttributeError
#  when adding invalid offset
offset = Week(weekday=1)
other = Day()
with pytest.raises(TypeError, match="Cannot add"):
    offset + other
