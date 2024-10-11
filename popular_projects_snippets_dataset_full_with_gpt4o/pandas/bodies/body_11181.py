# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# Fix following 30253
dti = date_range("2016-01-01", periods=2, name="foo")
df = DataFrame({("A", "B"): [1, 2], ("A", "C"): [1, 3], ("D", "B"): [0, 0]})
df.columns.names = ("bar", "baz")
df.index = dti

axis_number = df._get_axis_number(axis)
if not axis_number:
    df = df.T

gb = df.groupby(axis=axis_number, level=0)
result = gb.nunique()

expected = DataFrame({"A": [1, 2], "D": [1, 1]}, index=dti)
expected.columns.name = "bar"
if not axis_number:
    expected = expected.T

tm.assert_frame_equal(result, expected)

if axis_number == 0:
    # same thing, but empty columns
    gb2 = df[[]].groupby(axis=axis_number, level=0)
    exp = expected[[]]
else:
    # same thing, but empty rows
    gb2 = df.loc[[]].groupby(axis=axis_number, level=0)
    # default for empty when we can't infer a dtype is float64
    exp = expected.loc[[]].astype(np.float64)

res = gb2.nunique()
tm.assert_frame_equal(res, exp)
