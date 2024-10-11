# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
with pytest.raises(IndexingError, match="Too many indexers"):
    float_frame.iloc[:, :, :]

with pytest.raises(IndexError, match="too many indices for array"):
    # GH#32257 we let numpy do validation, get their exception
    float_frame.iloc[:, :, :] = 1
