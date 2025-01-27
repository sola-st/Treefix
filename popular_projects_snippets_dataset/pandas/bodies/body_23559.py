# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
        Generate the binary representation of the value labels.

        Parameters
        ----------
        byteorder : str
            Byte order of the output

        Returns
        -------
        value_label : bytes
            Bytes containing the formatted value label
        """
encoding = self._encoding
bio = BytesIO()
null_byte = b"\x00"

# len
bio.write(struct.pack(byteorder + "i", self.len))

# labname
labname = str(self.labname)[:32].encode(encoding)
lab_len = 32 if encoding not in ("utf-8", "utf8") else 128
labname = _pad_bytes(labname, lab_len + 1)
bio.write(labname)

# padding - 3 bytes
for i in range(3):
    bio.write(struct.pack("c", null_byte))

# value_label_table
# n - int32
bio.write(struct.pack(byteorder + "i", self.n))

# textlen  - int32
bio.write(struct.pack(byteorder + "i", self.text_len))

# off - int32 array (n elements)
for offset in self.off:
    bio.write(struct.pack(byteorder + "i", offset))

# val - int32 array (n elements)
for value in self.val:
    bio.write(struct.pack(byteorder + "i", value))

# txt - Text labels, null terminated
for text in self.txt:
    bio.write(text + null_byte)

exit(bio.getvalue())
