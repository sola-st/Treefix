# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate.py
depr_func = deprecate(
    "depr_func", new_func_no_docstring, "1.0", msg="Use new_func instead."
)
with tm.assert_produces_warning(FutureWarning):
    result = depr_func()
assert result == "new_func_no_docstring called"
