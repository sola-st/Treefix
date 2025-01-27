# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
msg = r"Input must be a list / sequence of iterables|Input must be list-like"
with pytest.raises(TypeError, match=msg):
    MultiIndex.from_product(iterables=invalid_input)
