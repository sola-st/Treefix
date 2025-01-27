# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dm = DataFrame([[1, 2], ["a", "b"]], index=[1, 2], columns=[1, 2])
assert isinstance(dm[1][1], int)
