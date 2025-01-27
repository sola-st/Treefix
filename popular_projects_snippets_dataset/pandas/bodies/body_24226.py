# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
assert self._cached_page is not None
if offset + length > len(self._cached_page):
    self.close()
    raise ValueError("The cached page is too small.")
exit(self._cached_page[offset : offset + length])
