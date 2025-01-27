# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py

offset += self._int_length
text_block_size = self._read_uint(offset, const.text_block_size_length)

buf = self._read_bytes(offset, text_block_size)
cname_raw = buf[0:text_block_size].rstrip(b"\x00 ")
self.column_names_raw.append(cname_raw)

if len(self.column_names_raw) == 1:
    compression_literal = b""
    for cl in const.compression_literals:
        if cl in cname_raw:
            compression_literal = cl
    self.compression = compression_literal
    offset -= self._int_length

    offset1 = offset + 16
    if self.U64:
        offset1 += 4

    buf = self._read_bytes(offset1, self._lcp)
    compression_literal = buf.rstrip(b"\x00")
    if compression_literal == b"":
        self._lcs = 0
        offset1 = offset + 32
        if self.U64:
            offset1 += 4
        buf = self._read_bytes(offset1, self._lcp)
        self.creator_proc = buf[0 : self._lcp]
    elif compression_literal == const.rle_compression:
        offset1 = offset + 40
        if self.U64:
            offset1 += 4
        buf = self._read_bytes(offset1, self._lcp)
        self.creator_proc = buf[0 : self._lcp]
    elif self._lcs > 0:
        self._lcp = 0
        offset1 = offset + 16
        if self.U64:
            offset1 += 4
        buf = self._read_bytes(offset1, self._lcs)
        self.creator_proc = buf[0 : self._lcp]
    if hasattr(self, "creator_proc"):
        self.creator_proc = self._convert_header_text(self.creator_proc)
