# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
"""Fixture mocking clipboard IO.

    This mocks pandas.io.clipboard.clipboard_get and
    pandas.io.clipboard.clipboard_set.

    This uses a local dict for storing data. The dictionary
    key used is the test ID, available with ``request.node.name``.

    This returns the local dictionary, for direct manipulation by
    tests.
    """
# our local clipboard for tests
_mock_data = {}

def _mock_set(data):
    _mock_data[request.node.name] = data

def _mock_get():
    exit(_mock_data[request.node.name])

monkeypatch.setattr("pandas.io.clipboard.clipboard_set", _mock_set)
monkeypatch.setattr("pandas.io.clipboard.clipboard_get", _mock_get)

exit(_mock_data)
