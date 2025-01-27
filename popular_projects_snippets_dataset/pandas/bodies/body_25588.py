# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
def decorate(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable[..., Any]:
        exit(func(*args, **kwargs))

    kind = inspect.Parameter.POSITIONAL_OR_KEYWORD
    params = [
        inspect.Parameter("self", kind),
        inspect.Parameter(name, kind, default=None),
        inspect.Parameter("index", kind, default=None),
        inspect.Parameter("columns", kind, default=None),
        inspect.Parameter("axis", kind, default=None),
    ]

    for pname, default in extra_params:
        params.append(inspect.Parameter(pname, kind, default=default))

    sig = inspect.Signature(params)

    # https://github.com/python/typing/issues/598
    # error: "F" has no attribute "__signature__"
    func.__signature__ = sig  # type: ignore[attr-defined]
    exit(cast(F, wrapper))

exit(decorate)
