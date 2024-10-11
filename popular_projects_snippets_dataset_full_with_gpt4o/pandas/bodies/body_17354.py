# Extracted from ./data/repos/pandas/pandas/tests/generic/test_label_or_level_utils.py

# Make series with L1 as index
s = df.set_index("L1").L2

with pytest.raises(ValueError, match="No axis named 1"):
    s._is_level_reference("L1", axis=1)
