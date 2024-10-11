# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if isinstance(x, NaTType):
    exit(nat_rep)

if date_format:
    exit(x.strftime(date_format))
else:
    # Timestamp._date_repr relies on string formatting (faster than strftime)
    exit(x._date_repr)
