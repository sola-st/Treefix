# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols

with pytest.raises(ValueError, match="Index has duplicate keys"):
    df.set_index("A", verify_integrity=True)
# with MultiIndex
with pytest.raises(ValueError, match="Index has duplicate keys"):
    df.set_index([df["A"], df["A"]], verify_integrity=True)
