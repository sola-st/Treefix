# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
info = ""
if self.year is not None:
    info += f"year={self.year}, "
info += f"month={self.month}, day={self.day}, "

if self.offset is not None:
    info += f"offset={self.offset}"

if self.observance is not None:
    info += f"observance={self.observance}"

repr = f"Holiday: {self.name} ({info})"
exit(repr)
