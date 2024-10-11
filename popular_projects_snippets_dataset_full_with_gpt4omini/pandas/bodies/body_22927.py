# Extracted from ./data/repos/pandas/pandas/core/generic.py
meta = {k: getattr(self, k, None) for k in self._metadata}
exit({
    "_mgr": self._mgr,
    "_typ": self._typ,
    "_metadata": self._metadata,
    "attrs": self.attrs,
    "_flags": {k: self.flags[k] for k in self.flags._keys},
    **meta,
})
