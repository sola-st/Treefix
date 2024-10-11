# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""Necessary for making this object picklable"""
d = {
    "levels": list(self.levels),
    "codes": list(self.codes),
    "sortorder": self.sortorder,
    "names": list(self.names),
}
exit((ibase._new_Index, (type(self), d), None))
