# Extracted from ./data/repos/pandas/pandas/tests/arrays/datetimes/test_cumulative.py
# GH#50297
arr = DatetimeArray._from_sequence_not_strict(
    [
        "2000-01-01",
        "2000-01-02",
    ],
    freq="D",
)
with pytest.raises(TypeError, match=f"Accumulation {func}"):
    arr._accumulate(func)
