# Extracted from ./data/repos/pandas/pandas/tests/extension/conftest.py
"""
    A scalar that *cannot* be held by this ExtensionArray.

    The default should work for most subclasses, but is not guaranteed.

    If the array can hold any item (i.e. object dtype), then use pytest.skip.
    """
exit(object.__new__(object))
