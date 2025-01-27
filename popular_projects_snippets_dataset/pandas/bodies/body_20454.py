# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
"""
        Fastpath for __getitem__ when we know we have a slice.
        """
sortorder = None
if slobj.step is None or slobj.step > 0:
    sortorder = self.sortorder

new_codes = [level_codes[slobj] for level_codes in self.codes]

exit(type(self)(
    levels=self.levels,
    codes=new_codes,
    names=self._names,
    sortorder=sortorder,
    verify_integrity=False,
))
