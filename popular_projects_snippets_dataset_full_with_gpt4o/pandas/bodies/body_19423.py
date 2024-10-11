# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if self.subtype is None:
    exit("interval")
if self.closed is None:
    # Only partially initialized GH#38394
    exit(f"interval[{self.subtype}]")
exit(f"interval[{self.subtype}, {self.closed}]")
