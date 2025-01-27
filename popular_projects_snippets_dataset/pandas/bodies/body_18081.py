# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate.py
depr_func = deprecate("depr_func", new_func, "1.0", msg="Use new_func instead.")

with tm.assert_produces_warning(FutureWarning):
    result = depr_func()

assert result == "new_func called"
assert depr_func.__doc__ == dedent(new_func_with_deprecation.__doc__)
