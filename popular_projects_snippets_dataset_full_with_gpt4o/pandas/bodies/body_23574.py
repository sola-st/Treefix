# Extracted from ./data/repos/pandas/pandas/io/stata.py
first_char = self.path_or_buf.read(1)
if struct.unpack("c", first_char)[0] == b"<":
    self._read_new_header()
else:
    self._read_old_header(first_char)

self.has_string_data = len([x for x in self.typlist if type(x) is int]) > 0

# calculate size of a data record
self.col_sizes = [self._calcsize(typ) for typ in self.typlist]
