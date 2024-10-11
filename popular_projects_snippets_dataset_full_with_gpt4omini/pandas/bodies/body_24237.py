# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
int_len = self._int_length
column_attributes_vectors_count = (length - 2 * int_len - 12) // (int_len + 8)
for i in range(column_attributes_vectors_count):
    col_data_offset = (
        offset + int_len + const.column_data_offset_offset + i * (int_len + 8)
    )
    col_data_len = (
        offset
        + 2 * int_len
        + const.column_data_length_offset
        + i * (int_len + 8)
    )
    col_types = (
        offset + 2 * int_len + const.column_type_offset + i * (int_len + 8)
    )

    x = self._read_uint(col_data_offset, int_len)
    self._column_data_offsets.append(x)

    x = self._read_uint(col_data_len, const.column_data_length_length)
    self._column_data_lengths.append(x)

    x = self._read_uint(col_types, const.column_type_length)
    self._column_types.append(b"d" if x == 1 else b"s")
