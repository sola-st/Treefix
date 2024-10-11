# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_coercion.py
index = pd.Index([3, 4], name="xxx")
obj = pd.Series(self.rep[from_key], index=index, name="yyy")
assert obj.dtype == from_key

if from_key.startswith("datetime") and to_key.startswith("datetime"):
    # tested below
    exit()
elif from_key in ["datetime64[ns, US/Eastern]", "datetime64[ns, UTC]"]:
    # tested below
    exit()

result = obj.replace(replacer)

if (from_key == "float64" and to_key in ("int64")) or (
    from_key == "complex128" and to_key in ("int64", "float64")
):

    if not IS64 or is_platform_windows():
        pytest.skip(f"32-bit platform buggy: {from_key} -> {to_key}")

    # Expected: do not downcast by replacement
    exp = pd.Series(self.rep[to_key], index=index, name="yyy", dtype=from_key)

else:
    exp = pd.Series(self.rep[to_key], index=index, name="yyy")
    assert exp.dtype == to_key

tm.assert_series_equal(result, exp)
