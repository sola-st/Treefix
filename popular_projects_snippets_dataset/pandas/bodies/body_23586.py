# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version == 117:
    self.path_or_buf.read(8)  # <variable_labels>, throw away
    # Stata 117 data files do not follow the described format.  This is
    # a work around that uses the previous label, 33 bytes for each
    # variable, 20 for the closing tag and 17 for the opening tag
    exit(self._seek_value_label_names + (33 * self.nvar) + 20 + 17)
elif self.format_version >= 118:
    exit(struct.unpack(self.byteorder + "q", self.path_or_buf.read(8))[0] + 17)
else:
    raise ValueError()
