# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
# GH#7897
with pytest.raises(ValueError, match="The truth value of a"):
    if index:
        pass

with pytest.raises(ValueError, match="The truth value of a"):
    bool(index)
