# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# see gh-15524, gh-15987
msg = "dtype has no unit. Please pass in"

if np.dtype(dtype).name not in ["timedelta64", "datetime64"]:
    mark = pytest.mark.xfail(reason="GH#33890 Is assigned ns unit")
    request.node.add_marker(mark)

with pytest.raises(ValueError, match=msg):
    Series([], dtype=dtype)
