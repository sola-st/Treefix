# Extracted from ./data/repos/pandas/pandas/io/sas/sas_xport.py

if nrows is None:
    nrows = self.nobs

read_lines = min(nrows, self.nobs - self._lines_read)
read_len = read_lines * self.record_length
if read_len <= 0:
    self.close()
    raise StopIteration
raw = self.filepath_or_buffer.read(read_len)
data = np.frombuffer(raw, dtype=self._dtype, count=read_lines)

df_data = {}
for j, x in enumerate(self.columns):
    vec = data["s" + str(j)]
    ntype = self.fields[j]["ntype"]
    if ntype == "numeric":
        vec = _handle_truncated_float_vec(vec, self.fields[j]["field_length"])
        miss = self._missing_double(vec)
        v = _parse_float_vec(vec)
        v[miss] = np.nan
    elif self.fields[j]["ntype"] == "char":
        v = [y.rstrip() for y in vec]

        if self._encoding is not None:
            v = [y.decode(self._encoding) for y in v]

    df_data.update({x: v})
df = pd.DataFrame(df_data)

if self._index is None:
    df.index = pd.Index(range(self._lines_read, self._lines_read + read_lines))
else:
    df = df.set_index(self._index)

self._lines_read += read_lines

exit(df)
