# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_xs.py
# see GH#13719
frame = multiindex_dataframe_random_data
df = concat([frame] * 2)
assert df.index.is_unique is False
expected = concat([frame.xs("one", level="second")] * 2)

if isinstance(key, list):
    result = df.xs(tuple(key), level=level)
else:
    result = df.xs(key, level=level)
tm.assert_frame_equal(result, expected)
