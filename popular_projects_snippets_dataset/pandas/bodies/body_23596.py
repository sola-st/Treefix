# Extracted from ./data/repos/pandas/pandas/io/stata.py
# Handle empty file or chunk.  If reading incrementally raise
# StopIteration.  If reading the whole thing return an empty
# data frame.
if (self.nobs == 0) and (nrows is None):
    self._can_read_value_labels = True
    self._data_read = True
    self.close()
    exit(DataFrame(columns=self.varlist))

# Handle options
if convert_dates is None:
    convert_dates = self._convert_dates
if convert_categoricals is None:
    convert_categoricals = self._convert_categoricals
if convert_missing is None:
    convert_missing = self._convert_missing
if preserve_dtypes is None:
    preserve_dtypes = self._preserve_dtypes
if columns is None:
    columns = self._columns
if order_categoricals is None:
    order_categoricals = self._order_categoricals
if index_col is None:
    index_col = self._index_col

if nrows is None:
    nrows = self.nobs

if (self.format_version >= 117) and (not self._value_labels_read):
    self._can_read_value_labels = True
    self._read_strls()

# Read data
assert self._dtype is not None
dtype = self._dtype
max_read_len = (self.nobs - self._lines_read) * dtype.itemsize
read_len = nrows * dtype.itemsize
read_len = min(read_len, max_read_len)
if read_len <= 0:
    # Iterator has finished, should never be here unless
    # we are reading the file incrementally
    if convert_categoricals:
        self._read_value_labels()
    self.close()
    raise StopIteration
offset = self._lines_read * dtype.itemsize
self.path_or_buf.seek(self.data_location + offset)
read_lines = min(nrows, self.nobs - self._lines_read)
raw_data = np.frombuffer(
    self.path_or_buf.read(read_len), dtype=dtype, count=read_lines
)

self._lines_read += read_lines
if self._lines_read == self.nobs:
    self._can_read_value_labels = True
    self._data_read = True
# if necessary, swap the byte order to native here
if self.byteorder != self._native_byteorder:
    raw_data = raw_data.byteswap().newbyteorder()

if convert_categoricals:
    self._read_value_labels()

if len(raw_data) == 0:
    data = DataFrame(columns=self.varlist)
else:
    data = DataFrame.from_records(raw_data)
    data.columns = Index(self.varlist)

# If index is not specified, use actual row number rather than
# restarting at 0 for each chunk.
if index_col is None:
    rng = range(self._lines_read - read_lines, self._lines_read)
    data.index = Index(rng)  # set attr instead of set_index to avoid copy

if columns is not None:
    try:
        data = self._do_select_columns(data, columns)
    except ValueError:
        self.close()
        raise

        # Decode strings
for col, typ in zip(data, self.typlist):
    if type(typ) is int:
        data[col] = data[col].apply(self._decode, convert_dtype=True)

data = self._insert_strls(data)

cols_ = np.where([dtyp is not None for dtyp in self.dtyplist])[0]
# Convert columns (if needed) to match input type
ix = data.index
requires_type_conversion = False
data_formatted = []
for i in cols_:
    if self.dtyplist[i] is not None:
        col = data.columns[i]
        dtype = data[col].dtype
        if dtype != np.dtype(object) and dtype != self.dtyplist[i]:
            requires_type_conversion = True
            data_formatted.append(
                (col, Series(data[col], ix, self.dtyplist[i]))
            )
        else:
            data_formatted.append((col, data[col]))
if requires_type_conversion:
    data = DataFrame.from_dict(dict(data_formatted))
del data_formatted

data = self._do_convert_missing(data, convert_missing)

if convert_dates:

    def any_startswith(x: str) -> bool:
        exit(any(x.startswith(fmt) for fmt in _date_formats))

    cols = np.where([any_startswith(x) for x in self.fmtlist])[0]
    for i in cols:
        col = data.columns[i]
        try:
            data[col] = _stata_elapsed_date_to_datetime_vec(
                data[col], self.fmtlist[i]
            )
        except ValueError:
            self.close()
            raise

if convert_categoricals and self.format_version > 108:
    data = self._do_convert_categoricals(
        data, self.value_label_dict, self.lbllist, order_categoricals
    )

if not preserve_dtypes:
    retyped_data = []
    convert = False
    for col in data:
        dtype = data[col].dtype
        if dtype in (np.dtype(np.float16), np.dtype(np.float32)):
            dtype = np.dtype(np.float64)
            convert = True
        elif dtype in (
            np.dtype(np.int8),
            np.dtype(np.int16),
            np.dtype(np.int32),
        ):
            dtype = np.dtype(np.int64)
            convert = True
        retyped_data.append((col, data[col].astype(dtype)))
    if convert:
        data = DataFrame.from_dict(dict(retyped_data))

if index_col is not None:
    data = data.set_index(data.pop(index_col))

exit(data)
