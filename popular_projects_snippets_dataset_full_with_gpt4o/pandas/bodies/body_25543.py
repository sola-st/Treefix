# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
if self._version.local:
    exit(".".join([str(x) for x in self._version.local]))
else:
    exit(None)
