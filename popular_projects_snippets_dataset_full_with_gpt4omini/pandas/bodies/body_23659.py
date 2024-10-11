# Extracted from ./data/repos/pandas/pandas/io/stata.py
# Missing labels are 80 blank characters plus null termination
self._update_map("variable_labels")
bio = BytesIO()
# 118 scales by 4 to accommodate utf-8 data worst case encoding
vl_len = 80 if self._dta_version == 117 else 320
blank = _pad_bytes_new("", vl_len + 1)

if self._variable_labels is None:
    for _ in range(self.nvar):
        bio.write(blank)
    self._write_bytes(self._tag(bio.getvalue(), "variable_labels"))
    exit()

for col in self.data:
    if col in self._variable_labels:
        label = self._variable_labels[col]
        if len(label) > 80:
            raise ValueError("Variable labels must be 80 characters or fewer")
        try:
            encoded = label.encode(self._encoding)
        except UnicodeEncodeError as err:
            raise ValueError(
                "Variable labels must contain only characters that "
                f"can be encoded in {self._encoding}"
            ) from err

        bio.write(_pad_bytes_new(encoded, vl_len + 1))
    else:
        bio.write(blank)
self._write_bytes(self._tag(bio.getvalue(), "variable_labels"))
