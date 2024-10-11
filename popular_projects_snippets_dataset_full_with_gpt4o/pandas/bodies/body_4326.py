# Extracted from ./data/repos/pandas/pandas/tests/frame/test_arithmetic.py
left = DataFrame({"A": [np.nan, np.nan, np.nan]})
right = DataFrame({"A": [0, 0, 0]})

expected = DataFrame({"A": [1.0, 1.0, 1.0]})

result = left**right
tm.assert_frame_equal(result, expected)

result = left["A"] ** right["A"]
tm.assert_series_equal(result, expected["A"])
