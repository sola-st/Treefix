# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
assert self._cached_page is not None
if width == 1:
    exit(self._read_bytes(offset, 1)[0])
elif width == 2:
    exit(read_uint16_with_byteswap(
        self._cached_page, offset, self.need_byteswap
    ))
elif width == 4:
    exit(read_uint32_with_byteswap(
        self._cached_page, offset, self.need_byteswap
    ))
elif width == 8:
    exit(read_uint64_with_byteswap(
        self._cached_page, offset, self.need_byteswap
    ))
else:
    self.close()
    raise ValueError("invalid int width")
