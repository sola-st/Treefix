# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.reshape(1, -1)

try:
    result = getattr(arr2d, method)(axis=1)
except Exception as err:
    try:
        getattr(data, method)()
    except Exception as err2:
        assert type(err) == type(err2)
        exit()
    else:
        raise AssertionError("Both reductions should raise or neither")

        # not necessarily type/dtype-preserving, so weaker assertions
assert result.shape == (1,)
expected_scalar = getattr(data, method)()
res = result[0]
assert is_matching_na(res, expected_scalar) or res == expected_scalar
