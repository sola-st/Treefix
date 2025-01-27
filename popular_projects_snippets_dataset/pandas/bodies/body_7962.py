# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/23438
data = date_range("2017", periods=4, freq="M")
if box is None:
    data = data._values
elif box == "series":
    data = Series(data)

result = PeriodIndex(data, freq="D")
expected = PeriodIndex(
    ["2017-01-31", "2017-02-28", "2017-03-31", "2017-04-30"], freq="D"
)
tm.assert_index_equal(result, expected)
