# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_constructors.py
# GH 22420
with pytest.raises(TypeError, match="Input must be a DataFrame"):
    MultiIndex.from_frame(non_frame)
