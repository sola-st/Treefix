# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if notna(value):
    if abs(value) > threshold:
        exit(decimal_formatter(value))
    else:
        exit(decimal_formatter(0.0))
else:
    exit(self.na_rep)
