# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
with pytest.raises(ValueError, match="need to split"):
    create_mgr("a: category; b: category")

with pytest.raises(ValueError, match="need to split"):
    create_mgr("a: category2; b: category2")
