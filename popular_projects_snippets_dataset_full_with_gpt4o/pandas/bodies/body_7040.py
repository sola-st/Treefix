# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_constructors.py
msg = "must be called with a collection of some kind"
with pytest.raises(TypeError, match=msg):
    CategoricalIndex(data=1, categories=list("abcd"), ordered=False)
with pytest.raises(TypeError, match=msg):
    CategoricalIndex(categories=list("abcd"), ordered=False)
