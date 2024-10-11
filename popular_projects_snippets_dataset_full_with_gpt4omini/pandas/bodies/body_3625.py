# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
# GH 30399

# define dataframe with unique datetime index
df = DataFrame(
    np.random.randn(5, 3),
    columns=["a", "b", "c"],
    index=pd.date_range("2012", freq="H", periods=5),
)
# create dataframe with non-unique datetime index
df = df.iloc[[0, 2, 2, 3]].copy()

with pytest.raises(KeyError, match="not found in axis"):
    df.drop(["a", "b"])  # Dropping with labels not exist in the index
