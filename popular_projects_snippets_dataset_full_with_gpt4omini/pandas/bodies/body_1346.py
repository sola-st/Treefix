# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py

# GH 4017, non-unique indexing (on the axis)
df = DataFrame({"A": [0.1] * 3000, "B": [1] * 3000})
idx = np.arange(30) * 99
expected = df.iloc[idx]

df3 = concat([df, 2 * df, 3 * df])
result = df3.iloc[idx]

tm.assert_frame_equal(result, expected)

df2 = DataFrame({"A": [0.1] * 1000, "B": [1] * 1000})
df2 = concat([df2, 2 * df2, 3 * df2])

with pytest.raises(KeyError, match="not in index"):
    df2.loc[idx]
