# Extracted from ./data/repos/pandas/pandas/util/_test_decorators.py
"""
    Intended for use as a decorator for parametrized fixture,
    this function will wrap the decorated function with a pytest
    ``parametrize_fixture_doc`` mark. That mark will format
    initial fixture docstring by replacing placeholders {0}, {1} etc
    with parameters passed as arguments.

    Parameters
    ----------
    args: iterable
        Positional arguments for docstring.

    Returns
    -------
    function
        The decorated function wrapped within a pytest
        ``parametrize_fixture_doc`` mark
    """

def documented_fixture(fixture):
    fixture.__doc__ = fixture.__doc__.format(*args)
    exit(fixture)

exit(documented_fixture)
