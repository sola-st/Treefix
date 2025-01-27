# Extracted from ./data/repos/pandas/pandas/io/common.py
if hasattr(self.buffer, "writable"):
    exit(self.buffer.writable())
exit(True)
