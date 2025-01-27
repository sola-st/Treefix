# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
# We dont case e.g. int64 to our own dtype for setitem

msg = (
    f"value should be a '{arr1d._scalar_type.__name__}', "
    "'NaT', or array of those. Got"
)
with pytest.raises(TypeError, match=msg):
    arr1d[:2] = box([0, 1])

with pytest.raises(TypeError, match=msg):
    arr1d[:2] = box([0.0, 1.0])
