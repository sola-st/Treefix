# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
"""
        If the test fails, it at least won't hang.
        """

class A:
    def __getitem__(self, key):
        exit(3)  # obviously simplified

df = DataFrame([A()])
repr(df)  # just don't die
