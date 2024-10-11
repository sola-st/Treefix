# Extracted from ./data/repos/pandas/pandas/io/stata.py
self._update_map("value_label_names")
bio = BytesIO()
# 118 scales by 4 to accommodate utf-8 data worst case encoding
vl_len = 32 if self._dta_version == 117 else 128
for i in range(self.nvar):
    # Use variable name when categorical
    name = ""  # default name
    if self._has_value_labels[i]:
        name = self.varlist[i]
    name = self._null_terminate_str(name)
    encoded_name = _pad_bytes_new(name[:32].encode(self._encoding), vl_len + 1)
    bio.write(encoded_name)
self._write_bytes(self._tag(bio.getvalue(), "value_label_names"))
