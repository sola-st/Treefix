# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH#29069 check that name is hashable
# See also same-named test in tests.series.test_constructors
idx = simple_index
with pytest.raises(TypeError, match="Index.name must be a hashable type"):
    type(idx)(idx, name=[])
