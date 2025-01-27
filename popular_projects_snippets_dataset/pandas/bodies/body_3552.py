# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH#12261
df = DataFrame(0, columns=[], index=MultiIndex.from_product([[], []]))
with tm.assert_produces_warning(None):
    df.loc["b", "2"] = 1
    df.loc["a", "3"] = 1
result = df.sort_index().index.is_monotonic_increasing
assert result is True
