# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
# error: "None" has no attribute "groups"
exit(self.grouper.groups)  # type: ignore[attr-defined]
