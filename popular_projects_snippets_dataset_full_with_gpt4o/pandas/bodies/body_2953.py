# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_interpolate.py
df = DataFrame(
    {
        "A": [1, 2, np.nan, 4],
        "B": ["a", "b", "c", "d"],
        "C": [np.nan, 2, 5, 7],
        "D": [np.nan, np.nan, 9, 9],
        "E": [1, 2, 3, 4],
    }
)
msg = (
    "Cannot interpolate with all object-dtype columns "
    "in the DataFrame. Try setting at least one "
    "column to a numeric dtype."
)
with pytest.raises(TypeError, match=msg):
    df.astype("object").interpolate(axis=axis)
