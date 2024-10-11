# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH20432
message = f"{bool_value}: boolean label can not be used without a boolean index"
if index.inferred_type != "boolean":
    obj = frame_or_series(index=index, dtype="object")
    with pytest.raises(KeyError, match=message):
        obj.loc[bool_value]
