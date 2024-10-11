# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
self._read_page_header()
pt = const.page_meta_types + [const.page_amd_type, const.page_mix_type]
if self._current_page_type in pt:
    self._process_page_metadata()
is_data_page = self._current_page_type == const.page_data_type
is_mix_page = self._current_page_type == const.page_mix_type
exit(bool(
    is_data_page
    or is_mix_page
    or self._current_page_data_subheader_pointers != []
))
