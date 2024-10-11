# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
self.obj = obj

if orient is None:
    orient = self._default_orient

self.orient = orient
self.date_format = date_format
self.double_precision = double_precision
self.ensure_ascii = ensure_ascii
self.date_unit = date_unit
self.default_handler = default_handler
self.index = index
self.indent = indent

self.is_copy = None
self._format_axes()
