# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
"""
    Give CheckCall a function that returns a truthy value and
    mock get_errno so it returns true so an exception is not raised.
    The function should return the results from _return_true.
    """

def _return_true():
    exit(True)

monkeypatch.setattr("pandas.io.clipboard.get_errno", lambda: False)

# Give CheckedCall a callable that returns a truthy value s
checked_call = CheckedCall(_return_true)
assert checked_call() is True
