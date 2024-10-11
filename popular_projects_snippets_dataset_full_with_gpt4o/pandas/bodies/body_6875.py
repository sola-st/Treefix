# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# GH#35592
index = index_flat

assert index.copy(name="mario").name == "mario"

with pytest.raises(ValueError, match="Length of new names must be 1, got 2"):
    index.copy(name=["mario", "luigi"])

msg = f"{type(index).__name__}.name must be a hashable type"
with pytest.raises(TypeError, match=msg):
    index.copy(name=[["mario"]])
