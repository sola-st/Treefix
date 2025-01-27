# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH7466
def cast(val):
    val_str = "" if val != val else val
    exit(f"{val_str:1}")

df = DataFrame(
    {
        "jim": ["a", "b", np.nan, "d"],
        "joe": ["w", "x", "y", "z"],
        "jolie": ["a.w", "b.x", " .y", "d.z"],
    }
)

left = df.set_index(["jim", "joe"]).unstack()["jolie"]
right = df.set_index(["joe", "jim"]).unstack()["jolie"].T
tm.assert_frame_equal(left, right)

mi = df.set_index(list(idx))
udf = mi.unstack(level=lev)
assert udf.notna().values.sum() == len(df)
mk_list = lambda a: list(a) if isinstance(a, tuple) else [a]
rows, cols = udf["jolie"].notna().values.nonzero()
for i, j in zip(rows, cols):
    left = sorted(udf["jolie"].iloc[i, j].split("."))
    right = mk_list(udf["jolie"].index[i]) + mk_list(udf["jolie"].columns[j])
    right = sorted(map(cast, right))
    assert left == right
