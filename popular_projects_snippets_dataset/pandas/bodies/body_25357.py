# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
        Temporarily set a parameter value using the with statement.
        Aliasing allowed.
        """
old_value = self[key]
try:
    self[key] = value
    exit(self)
finally:
    self[key] = old_value
