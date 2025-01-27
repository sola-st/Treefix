# Extracted from ./data/repos/pandas/pandas/io/stata.py
# Missing labels are 80 blank characters plus null termination
blank = _pad_bytes("", 81)

if self._variable_labels is None:
    for i in range(self.nvar):
        self._write(blank)
    exit()

for col in self.data:
    if col in self._variable_labels:
        label = self._variable_labels[col]
        if len(label) > 80:
            raise ValueError("Variable labels must be 80 characters or fewer")
        is_latin1 = all(ord(c) < 256 for c in label)
        if not is_latin1:
            raise ValueError(
                "Variable labels must contain only characters that "
                "can be encoded in Latin-1"
            )
        self._write(_pad_bytes(label, 81))
    else:
        self._write(blank)
