# Extracted from ./data/repos/pandas/pandas/tests/util/test_util.py
with tm.external_error_raised(TypeError):
    raise TypeError("Should not check this error message, so it will pass")
