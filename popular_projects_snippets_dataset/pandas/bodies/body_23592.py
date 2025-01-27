# Extracted from ./data/repos/pandas/pandas/io/stata.py
self.path_or_buf.seek(self.seek_strls)
# Wrap v_o in a string to allow uint64 values as keys on 32bit OS
self.GSO = {"0": ""}
while True:
    if self.path_or_buf.read(3) != b"GSO":
        break

    if self.format_version == 117:
        v_o = struct.unpack(self.byteorder + "Q", self.path_or_buf.read(8))[0]
    else:
        buf = self.path_or_buf.read(12)
        # Only tested on little endian file on little endian machine.
        v_size = 2 if self.format_version == 118 else 3
        if self.byteorder == "<":
            buf = buf[0:v_size] + buf[4 : (12 - v_size)]
        else:
            # This path may not be correct, impossible to test
            buf = buf[0:v_size] + buf[(4 + v_size) :]
        v_o = struct.unpack("Q", buf)[0]
    typ = struct.unpack("B", self.path_or_buf.read(1))[0]
    length = struct.unpack(self.byteorder + "I", self.path_or_buf.read(4))[0]
    va = self.path_or_buf.read(length)
    if typ == 130:
        decoded_va = va[0:-1].decode(self._encoding)
    else:
        # Stata says typ 129 can be binary, so use str
        decoded_va = str(va)
        # Wrap v_o in a string to allow uint64 values as keys on 32bit OS
    self.GSO[str(v_o)] = decoded_va
