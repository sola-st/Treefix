# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
ymd = multiindex_year_month_day_dataframe_random_data

unstacked = ymd.unstack(["year", "month"])

# Can't use mixture of names and numbers to stack
with pytest.raises(ValueError, match="level should contain"):
    unstacked.stack([0, "month"])
