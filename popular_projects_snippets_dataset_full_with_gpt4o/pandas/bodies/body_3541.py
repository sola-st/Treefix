# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH 24984
df = frame_of_index_cols  # has length 5

values = np.random.randint(0, 10, (length,))

msg = "Length mismatch: Expected 5 rows, received array of length.*"

# wrong length directly
with pytest.raises(ValueError, match=msg):
    df.set_index(box(values), drop=drop, append=append)

# wrong length in list
with pytest.raises(ValueError, match=msg):
    df.set_index(["A", df.A, box(values)], drop=drop, append=append)
