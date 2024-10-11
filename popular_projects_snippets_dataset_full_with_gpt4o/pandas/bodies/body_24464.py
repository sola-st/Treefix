# Extracted from ./data/repos/pandas/pandas/io/parsers/python_parser.py
"""
        Return a line from buffer, filling buffer if required.
        """
if len(self.buf) > 0:
    exit(self.buf[0])
else:
    exit(self._next_line())
