# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#39474
result = Series(["foo", "bar", "baz"]).astype(bytes)
assert result.dtypes == np.dtype("S3")
