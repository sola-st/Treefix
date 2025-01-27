# Extracted from ./data/repos/pandas/pandas/tests/base/test_misc.py
obj = index_or_series_obj

# Check that we work.
for p in ["shape", "dtype", "T", "nbytes"]:
    assert getattr(obj, p, None) is not None

# deprecated properties
for p in ["strides", "itemsize", "base", "data"]:
    assert not hasattr(obj, p)

msg = "can only convert an array of size 1 to a Python scalar"
with pytest.raises(ValueError, match=msg):
    obj.item()  # len > 1

assert obj.ndim == 1
assert obj.size == len(obj)

assert Index([1]).item() == 1
assert Series([1]).item() == 1
