# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_constructors.py
arr = DatetimeArray._from_sequence(
    ["2000"], dtype=DatetimeTZDtype(tz="US/Central")
)
with pytest.raises(TypeError, match="data is already tz-aware"):
    DatetimeArray._from_sequence_not_strict(
        arr, dtype=DatetimeTZDtype(tz="UTC")
    )
