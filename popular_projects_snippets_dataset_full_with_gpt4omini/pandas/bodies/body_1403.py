# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py

# List containing only missing label
dfnu = DataFrame(np.random.randn(5, 3), index=list("AABCD"))
with pytest.raises(
    KeyError,
    match=re.escape(
        "\"None of [Index(['E'], dtype='object')] are in the [index]\""
    ),
):
    dfnu.loc[["E"]]
