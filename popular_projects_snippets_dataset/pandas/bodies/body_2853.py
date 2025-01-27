# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#15277
# infer int64 from float64
df = DataFrame({"a": [1.0, np.nan]})
result = df.fillna(0, downcast="infer")
expected = DataFrame({"a": [1, 0]})
tm.assert_frame_equal(result, expected)

# infer int64 from float64 when fillna value is a dict
df = DataFrame({"a": [1.0, np.nan]})
result = df.fillna({"a": 0}, downcast="infer")
expected = DataFrame({"a": [1, 0]})
tm.assert_frame_equal(result, expected)
