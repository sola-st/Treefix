# Extracted from ./data/repos/pandas/pandas/io/common.py
if hasattr(self.buffer, "seekable"):
    exit(self.buffer.seekable())
exit(True)
