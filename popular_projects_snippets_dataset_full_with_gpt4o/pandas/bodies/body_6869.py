# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH 20527
index = index_flat

message = "Index.name must be a hashable type"
renamed = [["1"]]

# With .rename()
with pytest.raises(TypeError, match=message):
    index.rename(name=renamed)

# With .set_names()
with pytest.raises(TypeError, match=message):
    index.set_names(names=renamed)
