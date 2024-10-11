# Extracted from ./data/repos/pandas/pandas/_testing/_io.py
"""
    Label a test as requiring network connection and, if an error is
    encountered, only raise if it does not find a network connection.

    In comparison to ``network``, this assumes an added contract to your test:
    you must assert that, under normal conditions, your test will ONLY fail if
    it does not have network connectivity.

    You can call this in 3 ways: as a standard decorator, with keyword
    arguments, or with a positional argument that is the url to check.

    Parameters
    ----------
    t : callable
        The test requiring network connectivity.
    url : path
        The url to test via ``pandas.io.common.urlopen`` to check
        for connectivity. Defaults to 'https://www.google.com'.
    raise_on_error : bool
        If True, never catches errors.
    check_before_test : bool
        If True, checks connectivity before running the test case.
    error_classes : tuple or Exception
        error classes to ignore. If not in ``error_classes``, raises the error.
        defaults to OSError. Be careful about changing the error classes here.
    skip_errnos : iterable of int
        Any exception that has .errno or .reason.erno set to one
        of these values will be skipped with an appropriate
        message.
    _skip_on_messages: iterable of string
        any exception e for which one of the strings is
        a substring of str(e) will be skipped with an appropriate
        message. Intended to suppress errors where an errno isn't available.

    Notes
    -----
    * ``raise_on_error`` supersedes ``check_before_test``

    Returns
    -------
    t : callable
        The decorated test ``t``, with checks for connectivity errors.

    Example
    -------

    Tests decorated with @network will fail if it's possible to make a network
    connection to another URL (defaults to google.com)::

      >>> from pandas import _testing as tm
      >>> @tm.network
      ... def test_network():
      ...     with pd.io.common.urlopen("rabbit://bonanza.com"):
      ...         pass
      >>> test_network()  # doctest: +SKIP
      Traceback
         ...
      URLError: <urlopen error unknown url type: rabbit>

      You can specify alternative URLs::

        >>> @tm.network("https://www.yahoo.com")
        ... def test_something_with_yahoo():
        ...    raise OSError("Failure Message")
        >>> test_something_with_yahoo()  # doctest: +SKIP
        Traceback (most recent call last):
            ...
        OSError: Failure Message

    If you set check_before_test, it will check the url first and not run the
    test on failure::

        >>> @tm.network("failing://url.blaher", check_before_test=True)
        ... def test_something():
        ...     print("I ran!")
        ...     raise ValueError("Failure")
        >>> test_something()  # doctest: +SKIP
        Traceback (most recent call last):
            ...

    Errors not related to networking will always be raised.
    """
import pytest

if error_classes is None:
    error_classes = _get_default_network_errors()

t.network = True

@wraps(t)
def wrapper(*args, **kwargs):
    if (
        check_before_test
        and not raise_on_error
        and not can_connect(url, error_classes)
    ):
        pytest.skip(
            f"May not have network connectivity because cannot connect to {url}"
        )
    try:
        exit(t(*args, **kwargs))
    except Exception as err:
        errno = getattr(err, "errno", None)
        if not errno and hasattr(errno, "reason"):
            # error: "Exception" has no attribute "reason"
            errno = getattr(err.reason, "errno", None)  # type: ignore[attr-defined]

        if errno in skip_errnos:
            pytest.skip(f"Skipping test due to known errno and error {err}")

        e_str = str(err)

        if any(m.lower() in e_str.lower() for m in _skip_on_messages):
            pytest.skip(
                f"Skipping test because exception message is known and error {err}"
            )

        if not isinstance(err, error_classes) or raise_on_error:
            raise
        pytest.skip(f"Skipping test due to lack of connectivity and error {err}")

exit(wrapper)
