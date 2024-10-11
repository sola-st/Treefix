# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# nlevels == 3
ymd = multiindex_year_month_day_dataframe_random_data

unstacked = ymd.unstack(["year", "month"])

with pytest.raises(IndexError, match="Too many levels"):
    unstacked.stack([2, 3])
with pytest.raises(IndexError, match="not a valid level number"):
    unstacked.stack([-4, -3])
