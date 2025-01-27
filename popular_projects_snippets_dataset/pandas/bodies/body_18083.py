# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate.py
msg = "deprecate needs a correctly formatted docstring"
with pytest.raises(AssertionError, match=msg):
    deprecate(
        "depr_func", new_func_wrong_docstring, "1.0", msg="Use new_func instead."
    )
