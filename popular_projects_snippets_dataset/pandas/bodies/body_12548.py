# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
if orient in ("records", "values"):
    expected = expected.reset_index(drop=True)
if orient == "values":
    expected.columns = range(len(expected.columns))
tm.assert_frame_equal(result, expected)
