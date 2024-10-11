# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
ymd = multiindex_year_month_day_dataframe_random_data

result = ymd.groupby(level=[0, 1]).mean()

k1 = ymd.index.get_level_values(0)
k2 = ymd.index.get_level_values(1)

expected = ymd.groupby([k1, k2]).mean()

# TODO groupby with level_values drops names
tm.assert_frame_equal(result, expected, check_names=False)
assert result.index.names == ymd.index.names[:2]

result2 = ymd.groupby(level=ymd.index.names[:2]).mean()
tm.assert_frame_equal(result, result2)
