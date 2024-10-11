# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# gh-45601
df = DataFrame({"value": [42, None]}).astype({"value": "Int64"})
result = df.replace({pd.NA: None})
expected = DataFrame({"value": [42, None]}, dtype=object)
tm.assert_frame_equal(result, expected)
