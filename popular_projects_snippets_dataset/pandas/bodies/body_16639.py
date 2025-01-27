# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH#29130
left = pd.DataFrame({"x": data}, index=data)
right = pd.DataFrame({"x": data}, index=data)
with pytest.raises(
    MergeError,
    match=r"Incompatible merge dtype, .*, both sides must have numeric dtype",
):
    merge_asof(left, right, **kwargs)
