# Extracted from ./data/repos/pandas/pandas/io/stata.py
self.typlist = []
self.fmtlist = []
for col, dtype in dtypes.items():
    force_strl = col in self._convert_strl
    fmt = _dtype_to_default_stata_fmt(
        dtype,
        self.data[col],
        dta_version=self._dta_version,
        force_strl=force_strl,
    )
    self.fmtlist.append(fmt)
    self.typlist.append(
        _dtype_to_stata_type_117(dtype, self.data[col], force_strl)
    )
