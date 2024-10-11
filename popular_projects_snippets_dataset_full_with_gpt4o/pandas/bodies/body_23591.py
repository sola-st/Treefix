# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self._value_labels_read:
    # Don't read twice
    exit()
if self.format_version <= 108:
    # Value labels are not supported in version 108 and earlier.
    self._value_labels_read = True
    self.value_label_dict: dict[str, dict[float, str]] = {}
    exit()

if self.format_version >= 117:
    self.path_or_buf.seek(self.seek_value_labels)
else:
    assert self._dtype is not None
    offset = self.nobs * self._dtype.itemsize
    self.path_or_buf.seek(self.data_location + offset)

self._value_labels_read = True
self.value_label_dict = {}

while True:
    if self.format_version >= 117:
        if self.path_or_buf.read(5) == b"</val":  # <lbl>
            break  # end of value label table

    slength = self.path_or_buf.read(4)
    if not slength:
        break  # end of value label table (format < 117)
    if self.format_version <= 117:
        labname = self._decode(self.path_or_buf.read(33))
    else:
        labname = self._decode(self.path_or_buf.read(129))
    self.path_or_buf.read(3)  # padding

    n = struct.unpack(self.byteorder + "I", self.path_or_buf.read(4))[0]
    txtlen = struct.unpack(self.byteorder + "I", self.path_or_buf.read(4))[0]
    off = np.frombuffer(
        self.path_or_buf.read(4 * n), dtype=self.byteorder + "i4", count=n
    )
    val = np.frombuffer(
        self.path_or_buf.read(4 * n), dtype=self.byteorder + "i4", count=n
    )
    ii = np.argsort(off)
    off = off[ii]
    val = val[ii]
    txt = self.path_or_buf.read(txtlen)
    self.value_label_dict[labname] = {}
    for i in range(n):
        end = off[i + 1] if i < n - 1 else txtlen
        self.value_label_dict[labname][val[i]] = self._decode(txt[off[i] : end])
    if self.format_version >= 117:
        self.path_or_buf.read(6)  # </lbl>
self._value_labels_read = True
