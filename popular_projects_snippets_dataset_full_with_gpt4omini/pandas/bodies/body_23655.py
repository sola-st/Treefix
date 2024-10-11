# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("varnames")
bio = BytesIO()
# 118 scales by 4 to accommodate utf-8 data worst case encoding
vn_len = 32 if self._dta_version == 117 else 128
for name in self.varlist:
    name = self._null_terminate_str(name)
    name = _pad_bytes_new(name[:32].encode(self._encoding), vn_len + 1)
    bio.write(name)
self._write_bytes(self._tag(bio.getvalue(), "varnames"))
