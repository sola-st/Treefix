# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
bit_offset = self._page_bit_offset

for i in range(self._current_page_subheaders_count):
    offset = const.subheader_pointers_offset + bit_offset
    total_offset = offset + self._subheader_pointer_length * i

    subheader_offset = self._read_uint(total_offset, self._int_length)
    total_offset += self._int_length

    subheader_length = self._read_uint(total_offset, self._int_length)
    total_offset += self._int_length

    subheader_compression = self._read_uint(total_offset, 1)
    total_offset += 1

    subheader_type = self._read_uint(total_offset, 1)

    if (
        subheader_length == 0
        or subheader_compression == const.truncated_subheader_id
    ):
        continue

    subheader_signature = self._read_bytes(subheader_offset, self._int_length)
    subheader_index = get_subheader_index(subheader_signature)
    subheader_processor = self._subheader_processors[subheader_index]

    if subheader_processor is None:
        f1 = subheader_compression in (const.compressed_subheader_id, 0)
        f2 = subheader_type == const.compressed_subheader_type
        if self.compression and f1 and f2:
            self._current_page_data_subheader_pointers.append(
                (subheader_offset, subheader_length)
            )
        else:
            self.close()
            raise ValueError(
                f"Unknown subheader signature {subheader_signature}"
            )
    else:
        subheader_processor(subheader_offset, subheader_length)
