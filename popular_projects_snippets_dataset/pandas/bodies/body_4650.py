# Extracted from ./data/repos/pandas/pandas/tests/test_nanops.py
# Test numeric ndarray
values = np.array([1, 2, 3])
assert np.allclose(nanops._ensure_numeric(values), values)

# Test object ndarray
o_values = values.astype(object)
assert np.allclose(nanops._ensure_numeric(o_values), values)

# Test convertible string ndarray
s_values = np.array(["1", "2", "3"], dtype=object)
assert np.allclose(nanops._ensure_numeric(s_values), values)

# Test non-convertible string ndarray
s_values = np.array(["foo", "bar", "baz"], dtype=object)
msg = r"Could not convert .* to numeric"
with pytest.raises(TypeError, match=msg):
    nanops._ensure_numeric(s_values)
