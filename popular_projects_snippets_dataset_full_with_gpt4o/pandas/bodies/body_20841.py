# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
"""
        Fastpath for __getitem__ when we know we have a slice.
        """
res = self._data[slobj]
exit(type(self)._simple_new(res, name=self._name))
