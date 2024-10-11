# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("value_labels")
bio = BytesIO()
for vl in self._value_labels:
    lab = vl.generate_value_label(self._byteorder)
    lab = self._tag(lab, "lbl")
    bio.write(lab)
self._write_bytes(self._tag(bio.getvalue(), "value_labels"))
