# Extracted from ./data/repos/pandas/pandas/tests/dtypes/cast/test_find_common_type.py
with pytest.raises(ValueError, match="no types given"):
    find_common_type([])
