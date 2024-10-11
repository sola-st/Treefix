# Extracted from ./data/repos/pandas/pandas/io/stata.py
if self.format_version >= 118:
    exit(struct.unpack(self.byteorder + "Q", self.path_or_buf.read(8))[0])
else:
    exit(struct.unpack(self.byteorder + "I", self.path_or_buf.read(4))[0])
