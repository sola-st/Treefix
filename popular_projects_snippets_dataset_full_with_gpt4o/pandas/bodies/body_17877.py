# Extracted from ./data/repos/pandas/pandas/tests/util/test_validate_kwargs.py
good_arg = "f"
bad_arg = good_arg + "o"

compat_args = {good_arg: "foo", bad_arg + "o": "bar"}
kwargs = {good_arg: "foo", bad_arg: "bar"}

msg = rf"{_fname}\(\) got an unexpected keyword argument '{bad_arg}'"

with pytest.raises(TypeError, match=msg):
    validate_kwargs(_fname, kwargs, compat_args)
