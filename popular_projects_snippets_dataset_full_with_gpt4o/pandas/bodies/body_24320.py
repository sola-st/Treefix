# Extracted from ./data/repos/pandas/pandas/io/common.py
if hasattr(self.buffer, "readable"):
    exit(self.buffer.readable())
exit(True)
