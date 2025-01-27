# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py

# from SO
# https://stackoverflow.com/questions/24572040/pandas-access-the-level-of-multiindex-for-inplace-operation
df_orig = DataFrame.from_dict(
    {
        "price": {
            ("DE", "Coal", "Stock"): 2,
            ("DE", "Gas", "Stock"): 4,
            ("DE", "Elec", "Demand"): 1,
            ("FR", "Gas", "Stock"): 5,
            ("FR", "Solar", "SupIm"): 0,
            ("FR", "Wind", "SupIm"): 0,
        }
    }
)
df_orig.index = MultiIndex.from_tuples(
    df_orig.index, names=["Sit", "Com", "Type"]
)

expected = df_orig.copy()
expected.iloc[[0, 2, 3]] *= 2

idx = pd.IndexSlice
df = df_orig.copy()
df.loc[idx[:, :, "Stock"], :] *= 2
tm.assert_frame_equal(df, expected)

df = df_orig.copy()
df.loc[idx[:, :, "Stock"], "price"] *= 2
tm.assert_frame_equal(df, expected)
