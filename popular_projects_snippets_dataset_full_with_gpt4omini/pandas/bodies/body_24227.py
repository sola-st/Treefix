# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
exit(self._convert_header_text(
    self._read_bytes(offset, length).rstrip(b"\x00 ")
))
