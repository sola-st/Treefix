# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
iso_dates = self.date_format == "iso"
exit(dumps(
    self.obj_to_write,
    orient=self.orient,
    double_precision=self.double_precision,
    ensure_ascii=self.ensure_ascii,
    date_unit=self.date_unit,
    iso_dates=iso_dates,
    default_handler=self.default_handler,
    indent=self.indent,
))
