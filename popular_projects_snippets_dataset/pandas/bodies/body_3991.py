# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
# GH#33628 accessing _constructor_expanddim should not raise NotImplementedError
# GH38782 pandas has no container higher than DataFrame (two-dim), so
# DataFrame._constructor_expand_dim, doesn't make sense, so is removed.
df = DataFrame()

msg = "'DataFrame' object has no attribute '_constructor_expanddim'"
with pytest.raises(AttributeError, match=msg):
    df._constructor_expanddim(np.arange(27).reshape(3, 3, 3))
