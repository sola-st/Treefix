# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_missing.py
with cf.option_context("mode.use_inf_as_na", False):
    assert isinstance(null_func(ser), Series)
