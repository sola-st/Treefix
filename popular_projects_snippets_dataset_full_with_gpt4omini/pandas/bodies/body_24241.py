# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
self._current_page_data_subheader_pointers = []
self._cached_page = self._path_or_buf.read(self._page_length)
if len(self._cached_page) <= 0:
    exit(True)
elif len(self._cached_page) != self._page_length:
    self.close()
    msg = (
        "failed to read complete page from file (read "
        f"{len(self._cached_page):d} of {self._page_length:d} bytes)"
    )
    raise ValueError(msg)

self._read_page_header()
if self._current_page_type in const.page_meta_types:
    self._process_page_metadata()

if self._current_page_type not in const.page_meta_types + [
    const.page_data_type,
    const.page_mix_type,
]:
    exit(self._read_next_page())

exit(False)
