# Extracted from ./data/repos/pandas/pandas/compat/numpy/function.py
if args or kwargs:
    fname = self.fname if fname is None else fname
    max_fname_arg_count = (
        self.max_fname_arg_count
        if max_fname_arg_count is None
        else max_fname_arg_count
    )
    method = self.method if method is None else method

    if method == "args":
        validate_args(fname, args, max_fname_arg_count, self.defaults)
    elif method == "kwargs":
        validate_kwargs(fname, kwargs, self.defaults)
    elif method == "both":
        validate_args_and_kwargs(
            fname, args, kwargs, max_fname_arg_count, self.defaults
        )
    else:
        raise ValueError(f"invalid validation method '{method}'")
