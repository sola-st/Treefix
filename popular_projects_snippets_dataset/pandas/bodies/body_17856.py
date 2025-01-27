# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_args.py
msg = "'max_fname_arg_count' must be non-negative"

with pytest.raises(ValueError, match=msg):
    validate_args(_fname, (None,), -1, "foo")
