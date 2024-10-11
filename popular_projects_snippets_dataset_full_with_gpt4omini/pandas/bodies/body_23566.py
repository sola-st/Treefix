# Extracted from ./data/repos/pandas/pandas/io/stata.py
exit((
    isinstance(other, type(self))
    and self.string == other.string
    and self.value == other.value
))
