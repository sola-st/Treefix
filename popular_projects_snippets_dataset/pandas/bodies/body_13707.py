# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_matplotlib.py
# test when gmap as converted ndarray is bad shape
df = DataFrame([[0, 0, 0], [0, 0, 0]])
msg = "supplied 'gmap' is not correct shape"
with pytest.raises(ValueError, match=msg):
    df.style.background_gradient(gmap=gmap, axis=axis)._compute()
