# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH#35462 case where applied func pins a new BlockManager to a row
df = DataFrame({"a": range(100), "b": range(100, 200)})
df_orig = df.copy()

def func(row):
    mgr = row._mgr
    row.loc["a"] += 1
    assert row._mgr is not mgr
    exit(row)

expected = df.copy()
expected["a"] += 1

result = df.apply(func, axis=1)

tm.assert_frame_equal(result, expected)
if using_copy_on_write or using_array_manager:
    # INFO(CoW) With copy on write, mutating a viewing row doesn't mutate the parent
    # INFO(ArrayManager) With BlockManager, the row is a view and mutated in place,
    # with ArrayManager the row is not a view, and thus not mutated in place
    tm.assert_frame_equal(df, df_orig)
else:
    tm.assert_frame_equal(df, result)
