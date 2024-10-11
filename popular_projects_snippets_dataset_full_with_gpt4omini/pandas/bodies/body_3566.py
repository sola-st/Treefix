# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 43591
df = DataFrame({"a": [1, 2, 3]}, index=RangeIndex(4, -1, -2))
result = df.sort_index(
    ascending=False, ignore_index=ignore_index, inplace=inplace
)

if inplace:
    result = df
if ignore_index:
    expected = DataFrame({"a": [1, 2, 3]})
else:
    expected = DataFrame({"a": [1, 2, 3]}, index=RangeIndex(4, -1, -2))

tm.assert_frame_equal(result, expected)
