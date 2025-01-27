# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_find_common_type.py
result = find_common_type([left, right])

if left is right:
    assert result is left

elif left.subtype.kind in ["i", "u", "f"]:
    # i.e. numeric
    if right.subtype.kind in ["i", "u", "f"]:
        # both numeric -> common numeric subtype
        expected = IntervalDtype(np.float64, "right")
        assert result == expected
    else:
        assert result == object

else:
    assert result == object
