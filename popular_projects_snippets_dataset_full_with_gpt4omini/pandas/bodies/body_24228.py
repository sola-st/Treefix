# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
done = False
while not done:
    self._cached_page = self._path_or_buf.read(self._page_length)
    if len(self._cached_page) <= 0:
        break
    if len(self._cached_page) != self._page_length:
        raise ValueError("Failed to read a meta data page from the SAS file.")
    done = self._process_page_meta()
