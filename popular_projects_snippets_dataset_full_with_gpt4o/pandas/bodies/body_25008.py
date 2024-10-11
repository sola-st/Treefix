# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
formatter = self.formatter or get_format_timedelta64(
    self.values, nat_rep=self.nat_rep, box=self.box
)
exit([formatter(x) for x in self.values])
