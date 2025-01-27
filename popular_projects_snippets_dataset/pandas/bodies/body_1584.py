# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#40096
if not len(index):
    exit()

index = index.repeat(2)  # ensure non-unique
N = len(index)
arr = np.arange(N).astype(np.int64)

orig = DataFrame(arr, index=index, columns=[0])

# key that will requiring object-dtype casting in the index
key = "kapow"
assert key not in index  # otherwise test is invalid
# TODO: using a tuple key breaks here in many cases

exp_index = index.insert(len(index), key)
if isinstance(index, MultiIndex):
    assert exp_index[-1][0] == key
else:
    assert exp_index[-1] == key
exp_data = np.arange(N + 1).astype(np.float64)
expected = DataFrame(exp_data, index=exp_index, columns=[0])

# Add new row, but no new columns
df = orig.copy()
df.loc[key, 0] = N
tm.assert_frame_equal(df, expected)

# add new row on a Series
ser = orig.copy()[0]
ser.loc[key] = N
# the series machinery lets us preserve int dtype instead of float
expected = expected[0].astype(np.int64)
tm.assert_series_equal(ser, expected)

# add new row and new column
df = orig.copy()
df.loc[key, 1] = N
expected = DataFrame(
    {0: list(arr) + [np.nan], 1: [np.nan] * N + [float(N)]},
    index=exp_index,
)
tm.assert_frame_equal(df, expected)
