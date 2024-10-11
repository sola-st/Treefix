# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version >= 118:
    strlen = struct.unpack("b", self.path_or_buf.read(1))[0]
    exit(self.path_or_buf.read(strlen).decode("utf-8"))
elif self.format_version == 117:
    strlen = struct.unpack("b", self.path_or_buf.read(1))[0]
    exit(self._decode(self.path_or_buf.read(strlen)))
elif self.format_version > 104:
    exit(self._decode(self.path_or_buf.read(18)))
else:
    raise ValueError()
