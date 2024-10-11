# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
try:
    exit(self.get_chunk())
except StopIteration:
    self.close()
    raise
