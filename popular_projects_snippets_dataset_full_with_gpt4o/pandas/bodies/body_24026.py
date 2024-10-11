# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Parses a json document into a pandas object.
        """
typ = self.typ
dtype = self.dtype
kwargs = {
    "orient": self.orient,
    "dtype": self.dtype,
    "convert_axes": self.convert_axes,
    "convert_dates": self.convert_dates,
    "keep_default_dates": self.keep_default_dates,
    "precise_float": self.precise_float,
    "date_unit": self.date_unit,
    "use_nullable_dtypes": self.use_nullable_dtypes,
}
obj = None
if typ == "frame":
    obj = FrameParser(json, **kwargs).parse()

if typ == "series" or obj is None:
    if not isinstance(dtype, bool):
        kwargs["dtype"] = dtype
    obj = SeriesParser(json, **kwargs).parse()

exit(obj)
