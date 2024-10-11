# Extracted from ./data/repos/pandas/pandas/tests/test_flags.py
df = pd.DataFrame()
flags = df.flags
assert flags["allows_duplicate_labels"] is True
flags["allows_duplicate_labels"] = False
assert flags["allows_duplicate_labels"] is False

with pytest.raises(KeyError, match="a"):
    flags["a"]

with pytest.raises(ValueError, match="a"):
    flags["a"] = 10
