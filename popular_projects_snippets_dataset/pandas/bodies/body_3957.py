# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH#403
ymd = multiindex_year_month_day_dataframe_random_data
ymd["E"] = "foo"
ymd["F"] = 2

unstacked = ymd.unstack("month")
assert unstacked["A", 1].dtype == np.float64
assert unstacked["E", 1].dtype == np.object_
assert unstacked["F", 1].dtype == np.float64
