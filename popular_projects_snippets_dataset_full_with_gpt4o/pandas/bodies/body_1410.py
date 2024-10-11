# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_indexing.py
# GH 10610
df = DataFrame(np.random.random((10, 5)), columns=["a"] + [20, 21, 22, 23])

with pytest.raises(KeyError, match=re.escape("'[26, -8] not in index'")):
    df[[22, 26, -8]]
assert df[21].shape[0] == df.shape[0]
