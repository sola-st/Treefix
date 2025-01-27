# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
tuples = list(zip(float_frame["A"], float_frame["B"]))
float_frame["tuples"] = tuples

result = float_frame["tuples"]
expected = Series(tuples, index=float_frame.index, name="tuples")
tm.assert_series_equal(result, expected)
