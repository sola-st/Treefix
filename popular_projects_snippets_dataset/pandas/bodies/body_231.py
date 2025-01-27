# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 31466
df = DataFrame([[1.0, col]], columns=["a", "b"])
result = df.apply(lambda x: x.dtype)
expected = df.dtypes

tm.assert_series_equal(result, expected)
