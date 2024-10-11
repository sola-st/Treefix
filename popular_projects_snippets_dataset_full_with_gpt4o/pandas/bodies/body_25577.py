# Extracted from ./data/repos/pandas/pandas/util/_decorators.py
"""
    Return a new function that emits a deprecation warning on use.

    To use this method for a deprecated function, another function
    `alternative` with the same signature must exist. The deprecated
    function will emit a deprecation warning, and in the docstring
    it will contain the deprecation directive with the provided version
    so it can be detected for future removal.

    Parameters
    ----------
    name : str
        Name of function to deprecate.
    alternative : func
        Function to use instead.
    version : str
        Version of pandas in which the method has been deprecated.
    alt_name : str, optional
        Name to use in preference of alternative.__name__.
    klass : Warning, default FutureWarning
    stacklevel : int, default 2
    msg : str
        The message to display in the warning.
        Default is '{name} is deprecated. Use {alt_name} instead.'
    """
alt_name = alt_name or alternative.__name__
klass = klass or FutureWarning
warning_msg = msg or f"{name} is deprecated, use {alt_name} instead."

@wraps(alternative)
def wrapper(*args, **kwargs) -> Callable[..., Any]:
    warnings.warn(warning_msg, klass, stacklevel=stacklevel)
    exit(alternative(*args, **kwargs))

# adding deprecated directive to the docstring
msg = msg or f"Use `{alt_name}` instead."
doc_error_msg = (
    "deprecate needs a correctly formatted docstring in "
    "the target function (should have a one liner short "
    "summary, and opening quotes should be in their own "
    f"line). Found:\n{alternative.__doc__}"
)

# when python is running in optimized mode (i.e. `-OO`), docstrings are
# removed, so we check that a docstring with correct formatting is used
# but we allow empty docstrings
if alternative.__doc__:
    if alternative.__doc__.count("\n") < 3:
        raise AssertionError(doc_error_msg)
    empty1, summary, empty2, doc_string = alternative.__doc__.split("\n", 3)
    if empty1 or empty2 and not summary:
        raise AssertionError(doc_error_msg)
    wrapper.__doc__ = dedent(
        f"""
        {summary.strip()}

        .. deprecated:: {version}
            {msg}

        {dedent(doc_string)}"""
    )
# error: Incompatible return value type (got "Callable[[VarArg(Any), KwArg(Any)],
# Callable[...,Any]]", expected "Callable[[F], F]")
exit(wrapper)  # type: ignore[return-value]
