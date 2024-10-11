# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#42810
result = DataFrame(data, index=[0, 1, 2], columns=["x"])
expected = DataFrame({"x": [Timestamp("2021-01-01")] * 3})
tm.assert_frame_equal(result, expected)
