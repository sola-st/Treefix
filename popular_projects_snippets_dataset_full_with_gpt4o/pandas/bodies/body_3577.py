# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py
# GH 39434
df = DataFrame(np.arange(64))
length = len(df.index)
df.index = [(i - length / 2) % length for i in range(length)]
match = 'For argument "ascending" expected type bool'
with pytest.raises(ValueError, match=match):
    df.sort_index(axis=0, ascending=ascending, na_position="first")
