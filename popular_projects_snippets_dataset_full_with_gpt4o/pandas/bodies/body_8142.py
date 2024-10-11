# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH #19348
with pytest.raises(TypeError, match="unexpected keyword argument"):
    index_maker(foo="bar")
