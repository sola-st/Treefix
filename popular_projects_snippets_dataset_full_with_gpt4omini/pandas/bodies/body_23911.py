# Extracted from ./data/repos/pandas/pandas/io/pytables.py
try:
    exit((len(self.group.values),))
except (TypeError, AttributeError):
    exit(None)
