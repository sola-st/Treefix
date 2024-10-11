# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
with pytest.raises(ValueError, match="list"):
    DatetimeArray([1, 2, 3])
