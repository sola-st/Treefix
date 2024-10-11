# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH20432
message = (
    r"slice\(True, False, None\): boolean values can not be used in a slice"
)
obj = frame_or_series(index=index, dtype="object")
with pytest.raises(TypeError, match=message):
    obj.loc[True:False]
