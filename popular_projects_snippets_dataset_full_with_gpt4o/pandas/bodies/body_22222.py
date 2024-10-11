# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
self.key = key
self.level = level
self.freq = freq
self.axis = axis
self.sort = sort
self.dropna = dropna

self.grouper = None
self._gpr_index = None
self.obj = None
self.indexer = None
self.binner = None
self._grouper = None
self._indexer = None
