# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# see GH#15524, GH#15987
data = [1]
ser = Series(data)

if np.dtype(dtype).name not in ["timedelta64", "datetime64"]:
    mark = pytest.mark.xfail(reason="GH#33890 Is assigned ns unit")
    request.node.add_marker(mark)

msg = (
    rf"The '{dtype.__name__}' dtype has no unit\. "
    rf"Please pass in '{dtype.__name__}\[ns\]' instead."
)
with pytest.raises(ValueError, match=msg):
    ser.astype(dtype)
