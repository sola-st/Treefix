# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_dropna.py
# GH46575
df = DataFrame([1, 2, pd.NA])
msg = "You cannot set both the how and thresh arguments at the same time"
with pytest.raises(TypeError, match=msg):
    df.dropna(how="all", thresh=2)

with pytest.raises(TypeError, match=msg):
    df.dropna(how="any", thresh=2)

with pytest.raises(TypeError, match=msg):
    df.dropna(how=None, thresh=None)
