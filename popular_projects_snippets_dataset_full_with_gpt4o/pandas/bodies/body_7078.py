# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_any_index.py
names = index.nlevels * ["apple", "banana", "carrot"]
with pytest.raises(ValueError, match="^Length"):
    index.names = names
