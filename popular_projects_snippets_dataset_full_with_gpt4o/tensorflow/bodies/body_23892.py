# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
"""Returns all lines from the file in a list."""
self._preread_check()
lines = []
while True:
    s = self.readline()
    if not s:
        break
    lines.append(s)
exit(lines)
