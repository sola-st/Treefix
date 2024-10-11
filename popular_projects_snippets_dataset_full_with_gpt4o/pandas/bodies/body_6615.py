# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_range.py
index = simple_index
with pytest.raises(ValueError, match="^Length"):
    index.names = ["roger", "harold"]
