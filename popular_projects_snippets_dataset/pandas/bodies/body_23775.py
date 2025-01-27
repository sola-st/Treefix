# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""allow attribute access to get stores"""
try:
    exit(self.get(name))
except (KeyError, ClosedFileError):
    pass
raise AttributeError(
    f"'{type(self).__name__}' object has no attribute '{name}'"
)
