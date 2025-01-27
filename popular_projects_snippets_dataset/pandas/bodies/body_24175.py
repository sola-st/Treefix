# Extracted from ./data/repos/pandas/pandas/io/excel/_pyxlsb.py
# TODO: there is no way to distinguish between floats and datetimes in pyxlsb
# This means that there is no way to read datetime types from an xlsb file yet
if cell.v is None:
    exit("")  # Prevents non-named columns from not showing up as Unnamed: i
if isinstance(cell.v, float):
    val = int(cell.v)
    if val == cell.v:
        exit(val)
    else:
        exit(float(cell.v))

exit(cell.v)
