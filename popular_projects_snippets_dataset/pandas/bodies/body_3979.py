# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
f = float_frame

# reg name
expected = f.sum(axis=0)
result = f.sum(axis="index")
tm.assert_series_equal(result, expected)

expected = f.sum(axis=1)
result = f.sum(axis="columns")
tm.assert_series_equal(result, expected)
