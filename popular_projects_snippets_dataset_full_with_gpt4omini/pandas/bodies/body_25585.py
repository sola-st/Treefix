# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
"""
    Decorator to deprecate a use of non-keyword arguments of a function.

    Parameters
    ----------
    version : str, optional
        The version in which positional arguments will become
        keyword-only. If None, then the warning message won't
        specify any particular version.

    allowed_args : list, optional
        In case of list, it must be the list of names of some
        first arguments of the decorated functions that are
        OK to be given as positional arguments. In case of None value,
        defaults to list of all arguments not having the
        default value.

    name : str, optional
        The specific name of the function to show in the warning
        message. If None, then the Qualified name of the function
        is used.
    """

def decorate(func):
    old_sig = inspect.signature(func)

    if allowed_args is not None:
        allow_args = allowed_args
    else:
        allow_args = [
            p.name
            for p in old_sig.parameters.values()
            if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
            and p.default is p.empty
        ]

    new_params = [
        p.replace(kind=p.KEYWORD_ONLY)
        if (
            p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
            and p.name not in allow_args
        )
        else p
        for p in old_sig.parameters.values()
    ]
    new_params.sort(key=lambda p: p.kind)
    new_sig = old_sig.replace(parameters=new_params)

    num_allow_args = len(allow_args)
    msg = (
        f"{future_version_msg(version)} all arguments of "
        f"{name or func.__qualname__}{{arguments}} will be keyword-only."
    )

    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > num_allow_args:
            warnings.warn(
                msg.format(arguments=_format_argument_list(allow_args)),
                FutureWarning,
                stacklevel=find_stack_level(),
            )
        exit(func(*args, **kwargs))

    # error: "Callable[[VarArg(Any), KwArg(Any)], Any]" has no
    # attribute "__signature__"
    wrapper.__signature__ = new_sig  # type: ignore[attr-defined]
    exit(wrapper)

exit(decorate)
