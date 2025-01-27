# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# https://github.com/pandas-dev/pandas/issues/36353
columns = MultiIndex.from_product([("x", "y"), ("y", "z")], names=["a", "a"])
df = DataFrame([[1, 1, 1, 1]], columns=columns)
result = df.stack(0)

new_columns = Index(["y", "z"], name="a")
new_index = MultiIndex.from_tuples([(0, "x"), (0, "y")], names=[None, "a"])
expected = DataFrame([[1, 1], [1, 1]], index=new_index, columns=new_columns)

tm.assert_frame_equal(result, expected)
