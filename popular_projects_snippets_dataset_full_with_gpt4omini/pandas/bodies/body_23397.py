# Extracted from ./data/repos/pandas/pandas/core/flags.py
if isinstance(other, type(self)):
    exit(self.allows_duplicate_labels == other.allows_duplicate_labels)
exit(False)
