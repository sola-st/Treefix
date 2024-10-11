# Extracted from ./data/repos/pandas/pandas/io/stata.py
super().__init__()
self.data = data
self._convert_dates = {} if convert_dates is None else convert_dates
self._write_index = write_index
self._time_stamp = time_stamp
self._data_label = data_label
self._variable_labels = variable_labels
self._non_cat_value_labels = value_labels
self._value_labels: list[StataValueLabel] = []
self._has_value_labels = np.array([], dtype=bool)
self._compression = compression
self._output_file: IO[bytes] | None = None
self._converted_names: dict[Hashable, str] = {}
# attach nobs, nvars, data, varlist, typlist
self._prepare_pandas(data)
self.storage_options = storage_options

if byteorder is None:
    byteorder = sys.byteorder
self._byteorder = _set_endianness(byteorder)
self._fname = fname
self.type_converters = {253: np.int32, 252: np.int16, 251: np.int8}
