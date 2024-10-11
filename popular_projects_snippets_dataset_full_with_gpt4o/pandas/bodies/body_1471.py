# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
df = DataFrame({"a": [1]})
with pytest.raises(KeyError, match="\u05d0"):
    df.loc[:, "\u05d0"]  # should not raise UnicodeEncodeError
