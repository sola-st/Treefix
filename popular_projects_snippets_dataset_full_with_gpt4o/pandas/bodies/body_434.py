# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_common.py
# GH39010
assert not com.is_bool_dtype("0 - Name")
