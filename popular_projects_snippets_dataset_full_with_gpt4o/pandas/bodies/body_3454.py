# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
ymd = multiindex_year_month_day_dataframe_random_data

deleveled = ymd.reset_index(drop=True)
assert len(deleveled.columns) == len(ymd.columns)
assert deleveled.index.name == ymd.index.name
