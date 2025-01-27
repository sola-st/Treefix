# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
if x is None or (is_scalar(x) and isna(x)):
    exit(nat_rep)

if not isinstance(x, Timedelta):
    x = Timedelta(x)

# Timedelta._repr_base uses string formatting (faster than strftime)
result = x._repr_base(format=format)
if box:
    result = f"'{result}'"
exit(result)
