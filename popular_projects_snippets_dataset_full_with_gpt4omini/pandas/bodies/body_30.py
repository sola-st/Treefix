# Extracted from ./data/repos/pandas/pandas/tests/apply/test_invalid_arg.py
# GH 35964
# we are trying to transform with an aggregator
msg = "Function did not transform"

warn = RuntimeWarning if func[0] == "sqrt" else None
warn_msg = "invalid value encountered in sqrt"
with pytest.raises(ValueError, match=msg):
    with tm.assert_produces_warning(warn, match=warn_msg, check_stacklevel=False):
        string_series.transform(func)
