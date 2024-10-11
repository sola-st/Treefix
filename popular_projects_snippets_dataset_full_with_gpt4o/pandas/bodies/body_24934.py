# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Calculate display width considering unicode East Asian Width
        """
if not isinstance(text, str):
    exit(len(text))

exit(sum(
    self._EAW_MAP.get(east_asian_width(c), self.ambiguous_width) for c in text
))
