# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("formats")
bio = BytesIO()
fmt_len = 49 if self._dta_version == 117 else 57
for fmt in self.fmtlist:
    bio.write(_pad_bytes_new(fmt.encode(self._encoding), fmt_len))
self._write_bytes(self._tag(bio.getvalue(), "formats"))
