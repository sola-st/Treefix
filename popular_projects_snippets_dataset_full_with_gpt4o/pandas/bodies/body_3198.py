# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_get_numeric_data.py
# get the numeric data
obj = DataFrame({"A": [1, "2", 3.0]})
result = obj._get_numeric_data()
expected = DataFrame(dtype=object, index=pd.RangeIndex(3), columns=[])
tm.assert_frame_equal(result, expected)
