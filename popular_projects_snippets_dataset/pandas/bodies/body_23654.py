# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("variable_types")
bio = BytesIO()
for typ in self.typlist:
    bio.write(struct.pack(self._byteorder + "H", typ))
self._write_bytes(self._tag(bio.getvalue(), "variable_types"))
