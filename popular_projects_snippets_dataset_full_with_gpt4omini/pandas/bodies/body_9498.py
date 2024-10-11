# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_construction.py
with pytest.raises(ValueError, match="cannot be cast"):
    BooleanArray._from_sequence_of_strings(["donkey"])
