# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_dtype.py
with pytest.raises(ValueError, match=expected_error_msg):
    original.update_dtype(dtype)
