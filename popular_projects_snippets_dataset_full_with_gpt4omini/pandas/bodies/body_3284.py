# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# GH#39474
result = DataFrame(["foo", "bar", "baz"]).astype(bytes)
assert result.dtypes[0] == np.dtype("S3")
