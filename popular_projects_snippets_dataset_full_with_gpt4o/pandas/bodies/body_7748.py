# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH#42875
integer_index = Index([0, 1, 2, 3])
scalar_index = 1
msg = "Expected indices to be array-like"
with pytest.raises(TypeError, match=msg):
    integer_index.take(scalar_index)
