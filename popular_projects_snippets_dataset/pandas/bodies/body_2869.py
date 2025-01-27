# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#8377
df = DataFrame(
    {
        "a": [np.nan, 1, 2, np.nan, np.nan],
        "b": [1, 2, 3, np.nan, np.nan],
        "c": [np.nan, 1, 2, 3, 4],
    },
    index=list("VWXYZ"),
)

# df2 may have different index and columns
df2 = DataFrame(
    {
        "a": [np.nan, 10, 20, 30, 40],
        "b": [50, 60, 70, 80, 90],
        "foo": ["bar"] * 5,
    },
    index=list("VWXuZ"),
)

result = df.fillna(df2)

# only those columns and indices which are shared get filled
expected = DataFrame(
    {
        "a": [np.nan, 1, 2, np.nan, 40],
        "b": [1, 2, 3, np.nan, 90],
        "c": [np.nan, 1, 2, 3, 4],
    },
    index=list("VWXYZ"),
)

tm.assert_frame_equal(result, expected)
