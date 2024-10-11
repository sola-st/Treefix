# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
left = type(data)._concat_same_type([data, data]).reshape(-1, 2)
right = left.copy()

# axis=0
result = left._concat_same_type([left, right], axis=0)
expected = data._concat_same_type([data] * 4).reshape(-1, 2)
self.assert_extension_array_equal(result, expected)

# axis=1
result = left._concat_same_type([left, right], axis=1)
assert result.shape == (len(data), 4)
self.assert_extension_array_equal(result[:, :2], left)
self.assert_extension_array_equal(result[:, 2:], right)

# axis > 1 -> invalid
msg = "axis 2 is out of bounds for array of dimension 2"
with pytest.raises(ValueError, match=msg):
    left._concat_same_type([left, right], axis=2)
