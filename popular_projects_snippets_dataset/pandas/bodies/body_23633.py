# Extracted from ./data/repos/pandas/pandas/io/stata.py
# varlist names are checked by _check_column_names
# varlist, requires null terminated
for name in self.varlist:
    name = self._null_terminate_str(name)
    name = _pad_bytes(name[:32], 33)
    self._write(name)
