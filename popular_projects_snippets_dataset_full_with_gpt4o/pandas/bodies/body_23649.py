# Extracted from ./data/repos/pandas/pandas/io/stata.py
# Copy to new list since convert_strl might be modified later
self._convert_strl: list[Hashable] = []
if convert_strl is not None:
    self._convert_strl.extend(convert_strl)

super().__init__(
    fname,
    data,
    convert_dates,
    write_index,
    byteorder=byteorder,
    time_stamp=time_stamp,
    data_label=data_label,
    variable_labels=variable_labels,
    value_labels=value_labels,
    compression=compression,
    storage_options=storage_options,
)
self._map: dict[str, int] = {}
self._strl_blob = b""
