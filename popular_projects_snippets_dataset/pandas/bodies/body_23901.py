# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""retrieve our attributes"""
self.encoding = _ensure_encoding(getattr(self.attrs, "encoding", None))
self.errors = _ensure_decoded(getattr(self.attrs, "errors", "strict"))
for n in self.attributes:
    setattr(self, n, _ensure_decoded(getattr(self.attrs, n, None)))
