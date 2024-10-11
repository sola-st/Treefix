# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_normalize.py
# GH44312
# If errors="ignore" and nested metadata is null, we should return nan
data = {"meta": "foo", "nested_meta": None, "value": [{"rec": 1}, {"rec": 2}]}
result = json_normalize(
    data,
    record_path="value",
    meta=["meta", ["nested_meta", "leaf"]],
    errors="ignore",
)
ex_data = [[1, "foo", np.nan], [2, "foo", np.nan]]
columns = ["rec", "meta", "nested_meta.leaf"]
expected = DataFrame(ex_data, columns=columns).astype(
    {"nested_meta.leaf": object}
)
tm.assert_frame_equal(result, expected)

# If errors="raise" and nested metadata is null, we should raise with the
# key of the first missing level
with pytest.raises(KeyError, match="'leaf' not found"):
    json_normalize(
        data,
        record_path="value",
        meta=["meta", ["nested_meta", "leaf"]],
        errors="raise",
    )
