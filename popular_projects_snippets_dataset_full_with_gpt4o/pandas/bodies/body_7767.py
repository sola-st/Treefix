# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_drop_duplicates.py
# GH#10115
result = idx.drop_duplicates()
tm.assert_index_equal(idx, result)
assert idx.freq == result.freq

idx_dup = idx.append(idx)
result = idx_dup.drop_duplicates()

expected = idx
if not isinstance(idx, PeriodIndex):
    # freq is reset except for PeriodIndex
    assert idx_dup.freq is None
    assert result.freq is None
    expected = idx._with_freq(None)
else:
    assert result.freq == expected.freq

tm.assert_index_equal(result, expected)
