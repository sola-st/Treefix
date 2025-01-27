# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge_asof.py
# GH 23189
msg = f"Merge keys contain null values on {side} side"
nulls = func([1.0, 5.0, np.nan])
non_nulls = func([1.0, 5.0, 10.0])
df_null = pd.DataFrame({"a": nulls, "left_val": ["a", "b", "c"]})
df = pd.DataFrame({"a": non_nulls, "right_val": [1, 6, 11]})

with pytest.raises(ValueError, match=msg):
    if side == "left":
        merge_asof(df_null, df, on="a")
    else:
        merge_asof(df, df_null, on="a")
