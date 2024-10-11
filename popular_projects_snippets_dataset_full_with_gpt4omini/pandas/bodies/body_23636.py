# Extracted from ./data/repos/pandas/pandas/io/stata.py
# lbllist, 33*nvar, char array
for i in range(self.nvar):
    # Use variable name when categorical
    if self._has_value_labels[i]:
        name = self.varlist[i]
        name = self._null_terminate_str(name)
        name = _pad_bytes(name[:32], 33)
        self._write(name)
    else:  # Default is empty label
        self._write(_pad_bytes("", 33))
