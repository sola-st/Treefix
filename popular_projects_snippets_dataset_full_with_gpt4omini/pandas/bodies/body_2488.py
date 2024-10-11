# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#20410
mi = MultiIndex(
    levels=[["a_lot", "onlyone", "notevenone"], [1970, ""]],
    codes=[[1, 0], [1, 0]],
)
df = DataFrame(-1, index=range(3), columns=mi)

with pytest.raises(KeyError, match="notevenone"):
    df["notevenone"]
