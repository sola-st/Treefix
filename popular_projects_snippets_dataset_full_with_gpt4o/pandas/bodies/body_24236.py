# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
int_len = self._int_length
offset += int_len
column_name_pointers_count = (length - 2 * int_len - 12) // 8
for i in range(column_name_pointers_count):
    text_subheader = (
        offset
        + const.column_name_pointer_length * (i + 1)
        + const.column_name_text_subheader_offset
    )
    col_name_offset = (
        offset
        + const.column_name_pointer_length * (i + 1)
        + const.column_name_offset_offset
    )
    col_name_length = (
        offset
        + const.column_name_pointer_length * (i + 1)
        + const.column_name_length_offset
    )

    idx = self._read_uint(
        text_subheader, const.column_name_text_subheader_length
    )
    col_offset = self._read_uint(
        col_name_offset, const.column_name_offset_length
    )
    col_len = self._read_uint(col_name_length, const.column_name_length_length)

    name_raw = self.column_names_raw[idx]
    cname = name_raw[col_offset : col_offset + col_len]
    self.column_names.append(self._convert_header_text(cname))
