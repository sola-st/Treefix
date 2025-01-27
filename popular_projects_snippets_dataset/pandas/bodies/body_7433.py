# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
# GH19029
idx.names = ["foo", "foo"]
with pytest.raises(ValueError, match="name foo occurs multiple times"):
    idx._get_level_number("foo")
