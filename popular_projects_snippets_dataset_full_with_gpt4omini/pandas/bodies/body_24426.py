# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
if self.handles is not None:
    self.handles.close()
self._engine.close()
