# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_get.py
b = float_frame.get("B")
tm.assert_series_equal(b, float_frame["B"])

assert float_frame.get("foo") is None
tm.assert_series_equal(
    float_frame.get("foo", float_frame["B"]), float_frame["B"]
)
