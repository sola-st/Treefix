# Extracted from ./data/repos/pandas/pandas/tests/generic/test_frame.py
# GH8597
df = DataFrame(np.random.randn(5, 2), columns=["jim", "joe"])
ca = pd.Categorical([0, 0, 2, 2, 3, np.nan])
ts = df["joe"].copy()
ts[2] = np.nan

msg = "unexpected keyword"
with pytest.raises(TypeError, match=msg):
    df.drop("joe", axis=1, in_place=True)

with pytest.raises(TypeError, match=msg):
    df.reindex([1, 0], inplace=True)

with pytest.raises(TypeError, match=msg):
    ca.fillna(0, inplace=True)

with pytest.raises(TypeError, match=msg):
    ts.fillna(0, in_place=True)
