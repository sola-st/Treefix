# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_get.py
for obj in [string_series, object_series]:
    idx = obj.index[5]

    assert obj[idx] == obj.get(idx)
    assert obj[idx] == obj[5]

assert string_series.get(-1) == string_series.get(string_series.index[-1])
assert string_series[5] == string_series.get(string_series.index[5])
