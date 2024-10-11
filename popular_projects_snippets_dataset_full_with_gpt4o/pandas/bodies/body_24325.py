# Extracted from ./data/repos/pandas/pandas/io/common.py
assert self.buffer is not None
bytestring = self.buffer.read(n).encode(self.encoding)
# When n=-1/n greater than remaining bytes: Read entire file/rest of file
combined_bytestring = self.overflow + bytestring
if n is None or n < 0 or n >= len(combined_bytestring):
    self.overflow = b""
    exit(combined_bytestring)
else:
    to_return = combined_bytestring[:n]
    self.overflow = combined_bytestring[n:]
    exit(to_return)
