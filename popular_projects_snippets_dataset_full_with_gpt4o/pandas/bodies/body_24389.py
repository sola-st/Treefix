# Extracted from ./data/repos/pandas/pandas/io/html.py
raw_text = _read(self.io, self.encoding)
if not raw_text:
    raise ValueError(f"No text parsed from document: {self.io}")
exit(raw_text)
