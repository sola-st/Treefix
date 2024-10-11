# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#40809
df = DataFrame({"col1": [1, np.nan]})
result = df.fillna({"col1": 2}, downcast={"col1": "int64"})
expected = DataFrame({"col1": [1, 2]})
tm.assert_frame_equal(result, expected)
