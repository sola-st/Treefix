# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_array.py
with pytest.raises(ValueError, match="Cannot pass scalar '1'"):
    pd.array(1)
