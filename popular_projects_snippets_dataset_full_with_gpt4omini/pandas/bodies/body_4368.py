# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
df = DataFrame([[1, 2]])
should_be_view = DataFrame(df, dtype=df[0].dtype)
if using_copy_on_write:
    # TODO(CoW) doesn't mutate original
    should_be_view.iloc[0, 0] = 99
    # assert df.values[0, 0] == 1
    assert df.values[0, 0] == 99
else:
    should_be_view[0][0] = 99
    assert df.values[0, 0] == 99
