# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py
int_len = self._int_length
offset += int_len
self.column_count = self._read_uint(offset, int_len)
if self.col_count_p1 + self.col_count_p2 != self.column_count:
    print(
        f"Warning: column count mismatch ({self.col_count_p1} + "
        f"{self.col_count_p2} != {self.column_count})\n"
    )
