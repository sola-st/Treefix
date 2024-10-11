# Extracted from ./data/repos/pandas/pandas/core/computation/ops.py
# name is a str for Term, but may be something else for subclasses
self._name = name
self.env = env
self.side = side
tname = str(name)
self.is_local = tname.startswith(LOCAL_TAG) or tname in DEFAULT_GLOBALS
self._value = self._resolve_name()
self.encoding = encoding
