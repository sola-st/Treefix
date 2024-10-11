# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py

int_len = self._int_length
lcs_offset = offset
lcp_offset = offset
if self.U64:
    lcs_offset += 682
    lcp_offset += 706
else:
    lcs_offset += 354
    lcp_offset += 378

self.row_length = self._read_uint(
    offset + const.row_length_offset_multiplier * int_len,
    int_len,
)
self.row_count = self._read_uint(
    offset + const.row_count_offset_multiplier * int_len,
    int_len,
)
self.col_count_p1 = self._read_uint(
    offset + const.col_count_p1_multiplier * int_len, int_len
)
self.col_count_p2 = self._read_uint(
    offset + const.col_count_p2_multiplier * int_len, int_len
)
mx = const.row_count_on_mix_page_offset_multiplier * int_len
self._mix_page_row_count = self._read_uint(offset + mx, int_len)
self._lcs = self._read_uint(lcs_offset, 2)
self._lcp = self._read_uint(lcp_offset, 2)
