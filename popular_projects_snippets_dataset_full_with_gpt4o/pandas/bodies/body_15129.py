# Extracted from ./data/repos/pandas/pandas/tests/test_flags.py
df = pd.DataFrame()
flags = df.flags
del df
with pytest.raises(ValueError, match="object has been deleted"):
    flags.allows_duplicate_labels = True
