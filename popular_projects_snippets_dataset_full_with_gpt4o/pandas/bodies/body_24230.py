# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
bit_offset = self._page_bit_offset
tx = const.page_type_offset + bit_offset
self._current_page_type = (
    self._read_uint(tx, const.page_type_length) & const.page_type_mask2
)
tx = const.block_count_offset + bit_offset
self._current_page_block_count = self._read_uint(tx, const.block_count_length)
tx = const.subheader_count_offset + bit_offset
self._current_page_subheaders_count = self._read_uint(
    tx, const.subheader_count_length
)
