# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = float_string_frame
idx = Index(np.arange(len(df))[::-1])

df = df.set_index(idx)
tm.assert_index_equal(df.index, idx)
with pytest.raises(ValueError, match="Length mismatch"):
    df.set_index(idx[::2])
