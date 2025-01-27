# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture for a dictionary subclass.
    """

class TestSubDict(dict):
    def __init__(self, *args, **kwargs) -> None:
        dict.__init__(self, *args, **kwargs)

exit(TestSubDict)
