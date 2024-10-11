# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
"""
        Fastpath for __getitem__ when we know we have a slice.
        """
res = self._range[slobj]
exit(type(self)._simple_new(res, name=self._name))
