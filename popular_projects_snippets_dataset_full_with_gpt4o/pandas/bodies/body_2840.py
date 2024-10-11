# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
df = DataFrame(
    {"A": [np.nan] * 3, "B": [NaT, Timestamp(1), NaT], "C": [np.nan, "foo", 2]}
)
df.columns = ["A", "A", "A"]
orig = df[:]

df.fillna({"A": 2}, inplace=True)
# The first and third columns can be set inplace, while the second cannot.

expected = DataFrame(
    {"A": [2.0] * 3, "B": [2, Timestamp(1), 2], "C": [2, "foo", 2]}
)
expected.columns = ["A", "A", "A"]
tm.assert_frame_equal(df, expected)

# TODO: what's the expected/desired behavior with CoW?
if not using_copy_on_write:
    assert tm.shares_memory(df.iloc[:, 0], orig.iloc[:, 0])
assert not tm.shares_memory(df.iloc[:, 1], orig.iloc[:, 1])
if not using_copy_on_write:
    assert tm.shares_memory(df.iloc[:, 2], orig.iloc[:, 2])
