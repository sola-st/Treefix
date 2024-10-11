# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
df = DataFrame({"key": ["a"] * 3 + ["b"] * 3, "val": vals * 2})

# Figure out expectation using Python builtin
exp = getattr(builtins, agg_func)(vals)

# edge case for missing data with skipna and 'any'
if skipna and all(isna(vals)) and agg_func == "any":
    exp = False

exp_df = DataFrame([exp] * 2, columns=["val"], index=Index(["a", "b"], name="key"))
result = getattr(df.groupby("key"), agg_func)(skipna=skipna)
tm.assert_frame_equal(result, exp_df)
