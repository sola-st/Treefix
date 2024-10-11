# Extracted from ./data/repos/pandas/pandas/tests/series/test_validate.py
"""Tests for error handling related to data types of method arguments."""
msg = 'For argument "inplace" expected type bool'
kwargs = {"inplace": inplace}

if func == "_set_name":
    kwargs["name"] = "hello"

with pytest.raises(ValueError, match=msg):
    getattr(string_series, func)(**kwargs)
