# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_errors.py
msg = "Version is incorrect, expected sequence of 3 integers"
with pytest.raises(ValueError, match=msg):
    _maybe_adjust_name("values_block_0", version=bad_version)
