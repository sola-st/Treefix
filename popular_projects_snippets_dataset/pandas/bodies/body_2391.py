# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py

df = float_frame.copy()
df["$10"] = np.random.randn(len(df))

ad = np.random.randn(len(df))
df["@awesome_domain"] = ad

with pytest.raises(KeyError, match=re.escape("'df[\"$10\"]'")):
    df.__getitem__('df["$10"]')

res = df["@awesome_domain"]
tm.assert_numpy_array_equal(ad, res.values)
