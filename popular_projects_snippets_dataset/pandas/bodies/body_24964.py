# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Check whether the frame should be truncated. If so, slice the frame up.
        """
if self.is_truncated_horizontally:
    self._truncate_horizontally()

if self.is_truncated_vertically:
    self._truncate_vertically()
