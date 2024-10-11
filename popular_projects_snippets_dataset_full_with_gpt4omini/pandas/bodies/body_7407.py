# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
# GH12527
df_below_1000000 = pd.DataFrame(
    1, index=MultiIndex.from_product([[1, 2], range(499999)]), columns=["dest"]
)
with pytest.raises(KeyError, match=r"^\(-1, 0\)$"):
    df_below_1000000.loc[(-1, 0), "dest"]
with pytest.raises(KeyError, match=r"^\(3, 0\)$"):
    df_below_1000000.loc[(3, 0), "dest"]
df_above_1000000 = pd.DataFrame(
    1, index=MultiIndex.from_product([[1, 2], range(500001)]), columns=["dest"]
)
with pytest.raises(KeyError, match=r"^\(-1, 0\)$"):
    df_above_1000000.loc[(-1, 0), "dest"]
with pytest.raises(KeyError, match=r"^\(3, 0\)$"):
    df_above_1000000.loc[(3, 0), "dest"]
