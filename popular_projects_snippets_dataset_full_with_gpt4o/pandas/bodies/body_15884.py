# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#40732, GH#44940

floats = pd.Series([1.0, 2.0, 3.999, 4.4], dtype=pd.Float64Dtype())
assert floats.replace({1.0: 9}).dtype == floats.dtype
assert floats.replace(1.0, 9).dtype == floats.dtype
assert floats.replace({1.0: 9.0}).dtype == floats.dtype
assert floats.replace(1.0, 9.0).dtype == floats.dtype

res = floats.replace(to_replace=[1.0, 2.0], value=[9.0, 10.0])
assert res.dtype == floats.dtype

ints = pd.Series([1, 2, 3, 4], dtype=pd.Int64Dtype())
assert ints.replace({1: 9}).dtype == ints.dtype
assert ints.replace(1, 9).dtype == ints.dtype
assert ints.replace({1: 9.0}).dtype == ints.dtype
assert ints.replace(1, 9.0).dtype == ints.dtype

# nullable (for now) raises instead of casting
with pytest.raises(TypeError, match="Invalid value"):
    ints.replace({1: 9.5})
with pytest.raises(TypeError, match="Invalid value"):
    ints.replace(1, 9.5)
