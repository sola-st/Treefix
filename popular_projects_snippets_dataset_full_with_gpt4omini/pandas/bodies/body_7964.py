# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
idx = PeriodIndex([], freq="M")
assert isinstance(idx, PeriodIndex)
assert len(idx) == 0
assert idx.freq == "M"

with pytest.raises(ValueError, match="freq not specified"):
    PeriodIndex([])
