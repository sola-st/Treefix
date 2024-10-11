# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
assert self._cached_page is not None
if width == 4:
    exit(read_float_with_byteswap(
        self._cached_page, offset, self.need_byteswap
    ))
elif width == 8:
    exit(read_double_with_byteswap(
        self._cached_page, offset, self.need_byteswap
    ))
else:
    self.close()
    raise ValueError("invalid float width")
