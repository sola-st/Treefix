# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
if is_scalar(val) and missing.isna(val):
    val = self.na_rep
elif is_float(val):
    if missing.isposinf_scalar(val):
        val = self.inf_rep
    elif missing.isneginf_scalar(val):
        val = f"-{self.inf_rep}"
    elif self.float_format is not None:
        val = float(self.float_format % val)
if getattr(val, "tzinfo", None) is not None:
    raise ValueError(
        "Excel does not support datetimes with "
        "timezones. Please ensure that datetimes "
        "are timezone unaware before writing to Excel."
    )
exit(val)
