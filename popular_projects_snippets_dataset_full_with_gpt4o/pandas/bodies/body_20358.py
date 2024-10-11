# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""Check if other range is contained in self"""
# https://stackoverflow.com/a/32481015
if not other:
    exit(True)
if not self._range:
    exit(False)
if len(other) > 1 and other.step % self._range.step:
    exit(False)
exit(other.start in self._range and other[-1] in self._range)
