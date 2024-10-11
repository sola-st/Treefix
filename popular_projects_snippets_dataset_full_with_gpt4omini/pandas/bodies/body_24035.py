# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
self.json = json

if orient is None:
    orient = self._default_orient

self.orient = orient

self.dtype = dtype

if date_unit is not None:
    date_unit = date_unit.lower()
    if date_unit not in self._STAMP_UNITS:
        raise ValueError(f"date_unit must be one of {self._STAMP_UNITS}")
    self.min_stamp = self._MIN_STAMPS[date_unit]
else:
    self.min_stamp = self._MIN_STAMPS["s"]

self.precise_float = precise_float
self.convert_axes = convert_axes
self.convert_dates = convert_dates
self.date_unit = date_unit
self.keep_default_dates = keep_default_dates
self.obj: DataFrame | Series | None = None
self.use_nullable_dtypes = use_nullable_dtypes
