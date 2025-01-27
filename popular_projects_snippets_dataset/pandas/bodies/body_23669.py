# Extracted from ./data/repos/pandas/pandas/io/stata.py
if version is None:
    version = 118 if data.shape[1] <= 32767 else 119
elif version not in (118, 119):
    raise ValueError("version must be either 118 or 119.")
elif version == 118 and data.shape[1] > 32767:
    raise ValueError(
        "You must use version 119 for data sets containing more than"
        "32,767 variables"
    )

super().__init__(
    fname,
    data,
    convert_dates=convert_dates,
    write_index=write_index,
    byteorder=byteorder,
    time_stamp=time_stamp,
    data_label=data_label,
    variable_labels=variable_labels,
    value_labels=value_labels,
    convert_strl=convert_strl,
    compression=compression,
    storage_options=storage_options,
)
# Override version set in StataWriter117 init
self._dta_version = version
