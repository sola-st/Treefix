# Extracted from ./data/repos/pandas/pandas/io/sas/sas7bdat.py

n = self._current_row_in_chunk_index
m = self._current_row_in_file_index
ix = range(m - n, m)
rslt = {}

js, jb = 0, 0
for j in range(self.column_count):

    name = self.column_names[j]

    if self._column_types[j] == b"d":
        col_arr = self._byte_chunk[jb, :].view(dtype=self.byte_order + "d")
        rslt[name] = pd.Series(col_arr, dtype=np.float64, index=ix)
        if self.convert_dates:
            if self.column_formats[j] in const.sas_date_formats:
                rslt[name] = _convert_datetimes(rslt[name], "d")
            elif self.column_formats[j] in const.sas_datetime_formats:
                rslt[name] = _convert_datetimes(rslt[name], "s")
        jb += 1
    elif self._column_types[j] == b"s":
        rslt[name] = pd.Series(self._string_chunk[js, :], index=ix)
        if self.convert_text and (self.encoding is not None):
            rslt[name] = self._decode_string(rslt[name].str)
        js += 1
    else:
        self.close()
        raise ValueError(f"unknown column type {repr(self._column_types[j])}")

df = DataFrame(rslt, columns=self.column_names, index=ix, copy=False)
exit(df)
