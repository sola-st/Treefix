# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
df = DataFrame(
    [
        [1, np.nan, 2, 3],
        [4, np.nan, 5, 6],
        [np.nan, np.nan, np.nan, np.nan],
        [7, np.nan, 8, 9],
    ]
)

# GH20987
with pytest.raises(TypeError, match="supplying multiple axes"):
    df.dropna(how="all", axis=[0, 1])
with pytest.raises(TypeError, match="supplying multiple axes"):
    df.dropna(how="all", axis=(0, 1))

inp = df.copy()
with pytest.raises(TypeError, match="supplying multiple axes"):
    inp.dropna(how="all", axis=(0, 1), inplace=True)
