# Extracted from ./data/repos/pandas/pandas/tests/config/test_config.py

# the pandas object exposes the user API
assert hasattr(pd, "get_option")
assert hasattr(pd, "set_option")
assert hasattr(pd, "reset_option")
assert hasattr(pd, "describe_option")
